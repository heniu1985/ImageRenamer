import os, glob
import time

from PIL import Image
from PIL.ExifTags import TAGS

def get_photos():
    """Function creates a list of photos from given folder"""

    folder_path = input("Enter the path to the photo directory: ")
    pics_extension = input("Enter photo extension: ")
    pics_path = folder_path + "/*." + pics_extension

    pictures = glob.glob(pics_path)

    return pictures

