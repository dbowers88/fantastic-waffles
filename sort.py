from PIL import Image
import glob
import os
import shutil
import time

input ("Press any key to sort.")
#Get image dimensions
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    print ("", im.size)
    if im.size == (1920, 1080): #Match Width and Height, then move to corresponding folder.
        shutil.move(image_file, "16x9")
    elif im.size == (2560, 1080):
        shutil.move(image_file, "Ultrawide")
    elif im.size == (3440, 3440):
        shutil.move(image_file, "Ultrawide")
    elif im.size == (2560, 1440):
        shutil.move(image_file, "16x9")
    elif im.size == (1080, 1920):
        shutil.move(image_file, "Phone")
