from PIL import Image, ImageDraw
import os


# img = Image.open("hopper.jpg")
# img2 = Image.open("cat.webp")

# hopper = "hopper.jpg"
# cat = 'cat.webp'

# im = [img, img2]

# for x in im:
# 	draw = ImageDraw.Draw(im)
# 	draw.line((0, 0) + im.size, fill=128)
# 	draw.line((0, im.size[1], im.size[0], 0), fill=128)
# 	base = os.path.splitext(hopper, cat)[0]
# 	os.rename(hopper, cat, base + '.png')
# 	im.show()

class Drawing:
	def __init__(self,name):
		self.name = name
	def drawer(self):
		draw = ImageDraw.Draw(self)
		draw.line((0, 0) + self.size, fill=128)
		draw.line((0, self.size[1], self.size[0], 0), fill=128)
		base = os.path.splitext(self.name)[0]
		os.rename(self.name, base + '.png')
		self.show()
		print("Completed!")

class DrawingObj(Drawing):
	def __init__(self, name):
		self.name = name
		print("Completed1")
	drawer(self)


cat = DrawingObj('cat.webp')

hopper = DrawingObj('hopper.jpg')
