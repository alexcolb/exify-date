EXIFy Date
==========

This script updates the EXIF **DateTimeOriginal** field of a JPEG image. It copies the value from the unstable **Date Modified** field, and injects it into the EXIF data. This is useful when a camera (eg. Snapchat for Android) does not leverage EXIF values, as the **Date Modified** tends to be changed over time.


Installation & Usage
--------------------

Confirmed to work only on Windows 10. Begin by installing Piexif:
``pip install piexif``

To simply crunch all ``.jpg`` files, copy the python script into the desired directory and run 
``python exify-date.py``

Optional parameters may be added to the end of the command:
- ``-v`` Log verbosely.
- ``-d <directory>`` Work in a given subdirectory, eg. ``python exify-date.py -d photos``
- ``-e <extension>`` Look for a custom extension, eg. ``python exify-date.py -e jpeg``
