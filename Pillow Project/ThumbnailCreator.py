from __future__ import print_function
import os, sys
from PIL import Image

# size = (128, 128)

# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile, "JPEG")
#         except IOError:
#             print("cannot create thumbnail for", infile)

def thumbnail_converter(filename, height, width):
    size = (height, width)
    im = Image.open(filename).convert('RGB')
    im.thumbnail(size)
    im.save(filename + '.jpg', quality=95)
    im.show()

while True:
    user_input_filename = str(input("Enter file name: "))
    height = int(input("Enter desired height: "))
    width = int(input("Enter desired width: "))
    thumbnail_converter(user_input_filename, height, width)
    repeat_conversion = str(input("Continue?[y/n]: "))
    if repeat_conversion == 'n':
        break


