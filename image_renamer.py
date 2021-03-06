import os, glob
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

def get_photos(folder_path, pics_extension):
    """Function create a list of photos from given folder"""

    pics_path = folder_path + "/*." + pics_extension

    return glob.glob(pics_path)

def get_photos_taken_date(picture_list):
    """Function create a list whit photo taken date and time"""

    photos_taken_date = []
    no_date_number = 1
    repeat_date_number = 1
    for picture in picture_list:
        img = Image.open(picture)
        exif = img._getexif()
        try:
            if exif.get(36867) == None:
                photos_taken_date.append(f"No date - {no_date_number}")
                no_date_number += 1
            else:
                if exif.get(36867) not in photos_taken_date:
                    photos_taken_date.append(exif.get(36867))
                else:
                    photos_taken_date.append(exif.get(36867) + " - " + str(repeat_date_number))
                    repeat_date_number += 1
        except AttributeError:
            photos_taken_date.append(f"No date - {no_date_number}")
            no_date_number += 1

    return photos_taken_date

def rename_photos(old_name, folder_path, taken_date, file_extension):
    """Function reaname photo files names to their dates"""

    new_name = folder_path + "/" + taken_date + "." + file_extension
    os.rename(old_name, new_name)

def main():
    """Main program function"""

    path = input("Enter the path to the photo directory: ")
    extension = input("Enter photo extension: ")

    pictures = get_photos(path, extension)
    dates = get_photos_taken_date(pictures)

    if len(pictures) == len(dates) and len(dates) == len(set(dates)):
        for i in range(len(pictures)):
            rename_photos(pictures[i], path, dates[i], extension)
    else:
        print("Not all pictures have dates!!!")

main()