from PIL import Image
import glob
import os
import shutil
import time

#get and print current path
cpath = os.getcwd()
print ("Current directory:", cpath);

#get path from user
print ("Please input the path to folder:")
pathin = input();

if os.path.exists(pathin):
    os.chdir(pathin)
    print("Changed to path:", pathin)
elif not os.path.exists(pathin):
    print("Directory not found! Create Directory? Yes(1) or No(2):")
nopath = input()
usrin = "1"
if nopath == usrin:
    os.mkdir(pathin)
    os.chdir(pathin)
#else:
#    quit()

#Print current path
npath = os.getcwd()
inpath = os.listdir()
print ("Current directory:", npath)
print ("Files in directory:", inpath);
input ('Press any key to create folders for images.');

#Create Directories for sorting
newpath = r"16x9"
if os.path.exists(newpath):
    print ("1080P Folder already exists")
if not os.path.exists(newpath):
        os.makedirs(newpath)
newpath = r"OtherSizes"
if os.path.exists(newpath):
    print ("OtherSizes Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"Ultrawide"
if os.path.exists(newpath):
    print ("Ultrawide Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"4x3"
if os.path.exists(newpath):
    print ("4x3 Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"4K"
if os.path.exists(newpath):
    print("4K Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"16x10"
if os.path.exists(newpath):
    print("16x10 Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)

input ("Press any key to sort.")
#Get image dimensions
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    print ("", im.size)
    if im.size == (1920, 1080): #Match Width and Height, then move to corresponding folder.
        shutil.move(image_file, "16x9")
    elif im.size == (2560, 1440):
        shutil.move(image_file, "16x9")
    elif im.size == (1360, 768):
        shutil.move(image_file, "16x9")
    elif im.size == (1366, 768):
        shutil.move(image_file, "16x9")
    elif im.size == (1600, 900):
        shutil.move(image_file, "16x9")
    elif im.size == (2560, 1080):
        shutil.move(image_file, "Ultrawide")
    elif im.size == (3440, 1440):
        shutil.move(image_file, "Ultrawide")
    elif im.size == (1900, 1200):
        shutil.move(image_file, "16x10")
    elif im.size == (2560, 1600):
        shutil.move(image_file, "16x10")
    elif im.size == (1920, 1200):
        shutil.move(image_file, "16x10")
    elif im.size == (1680, 1050):
        shutil.move(image_file, "16x10")
    elif im.size == (1440, 900):
        shutil.move(image_file, "16x10")
    elif im.size == (1280, 960):
        shutil.move(image_file, "4x3")
    elif im.size == (1024, 768):
        shutil.move(image_file, "4x3")
    elif im.size == (1280, 1024):
        shutil.move(image_file, "4x3")
    elif im.size == (800, 600):
        shutil.move(image_file, "4x3")
    elif im.size == (3840, 2160):
        shutil.move(image_file, "4K")
    else:
        shutil.move(image_file, "OtherSizes")
