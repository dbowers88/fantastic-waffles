from PIL import Image
import glob
import os
#calculate r for height and Width
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    h = im.height
    w = im.width
def ratio(h, w):
    h = float(h)
    w = float(w)
    if w == 0:
        return a
    return ratio(b, a % b)

#return string with ratio for height and Width
def get_ratio(h, w):
    r = ratio(h, w)
    return(print("%s" % float((h/r) / (w /r))))
