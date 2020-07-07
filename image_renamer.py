import os, glob
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

def get_photos():
    """Function create a list of photos from given folder"""

    folder_path = input("Enter the path to the photo directory: ")
    pics_extension = input("Enter photo extension: ")
    pics_path = folder_path + "/*." + pics_extension

    return glob.glob(pics_path)

def get_photo_taken_date():
    """Function create a list whit photo taken date and time"""

    taken_date = []
    for picture in pictures:
        img = Image.open(picture)
        exif = img._getexif()
        taken_date.append(exif.get("DateTimeOriginal"))

        return taken_date