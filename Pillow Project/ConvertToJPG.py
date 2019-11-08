from __future__ import print_function
import os, sys
from PIL import Image

# for infile in sys.argv[1:]:
# 	f, e = os.path.splitext(infile)
# 	outfile = f + ".jpg"
# 	if infile != outfile:
# 		try:
# 			Image.open(infile).save(outfile)
# 		except IOError:
# 			print("Cannot convert", infile)

def jpg_convert(file_name):
	try:
		im = Image.open(file_name)
		bg = Image.new("RGB", im.size, (255,255,255))
		bg.paste(im, box=None, mask=0)
		bg.save(file_name + ".jpg", quality=95)
	except IOError:
		print("Cannot convert to jpg!")

while True:
	user_input_filename = input("Enter file name: ")
	jpg_convert(user_input_filename)
	repeat_conversion = input("Continue?[y/n]: ")
	if repeat_conversion == 'n':
		break


print("Completed!")