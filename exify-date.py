import piexif
import os
import sys
import time
import glob

# Method to get the paremeter value from arguments list
# Eg. for prepender "d": "python <script> -d photos" will return "photos"
def getParamValue(prepender):
	if "-{}".format(prepender) in sys.argv:
		index = sys.argv.index("-{}".format(prepender))
		value = sys.argv[index + 1] # IndexError on failure
		return value
	else:
		return None

def main():

	photoGlob = "*." # File match base
	verbose = False
	counter = 0

	# Read arguments

	directory = getParamValue("d")
	if directory is not None:
		prefix = directory
		if prefix[-1] != "/" and prefix[-1] != "\\":
			prefix += "/"
		print("Accessing directory {}".format(prefix))
		photoGlob = prefix + photoGlob 
	
	extension = getParamValue("e")
	if extension is not None:
		photoGlob += extension
		print("Using custom extension .{}".format(extension))
	else:
		photoGlob += "jpg" # Default extension


	if "-v" in sys.argv:
		print("Logging verbosely.")
		verbose = True

	# Iterate all matched files
	for file in glob.glob(photoGlob):
		ifd = "Exif"
		tag = 36867 # DateTimeOriginal

		exif_dict = piexif.load(file)

		if tag in exif_dict[ifd]:
			print("Already have EXIF data {} for {}".format(exif_dict[ifd][tag], file))
			continue
		
		stats = os.stat(file)
		modified = int(stats.st_mtime)

		toexif = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(modified)).encode("utf-8") 
		exif_dict[ifd][tag] = toexif

		exif_bytes = piexif.dump(exif_dict)

		if verbose:
			print("File {}: {} from {}".format(file, toexif, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modified))))

		piexif.insert(exif_bytes, file)
		counter += 1

	message = "Copied modification time to EXIF data for {}/{} files.".format(counter, len(glob.glob(photoGlob)))
	print("_" * len(message) + "\n")
	print(message)

main(
)