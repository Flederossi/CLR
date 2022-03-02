from PIL import Image

class Renderer():
	def renderIMG(event, img, size, qual):
		line = ""
		res = ""
		if qual == 3:
			charsnum = [0,128,256]
			chars = ["@","+","."]
		elif qual == 5:
			charsnum = [0,64,128,224,256]
			chars = ["@","#","+","-","."]
		elif qual == 9:
			charsnum = [0,32,64,96,128,160,192,224,256]
			chars = ["@","%","#","*","+","=","-",":","."]
		else:
			print("Invalid quality -> Allowed: 3,5,9")
			exit()
		im = Image.open(img).convert('LA')
		im.load()
		if im.size > size:
			im.thumbnail(size, Image.ANTIALIAS)
		width, height = im.size
		pixel_values = list(im.getdata())
		for y in range(height):
			for x in range(width):
				num = pixel_values[width*y+x][0]
				curr = charsnum[0]
				for val in charsnum:
					if abs(num - val) < abs(num - curr):
						curr = val
				line = line + " " + chars[charsnum.index(curr)]
			res += line + "\n"
			line = ""
		return res