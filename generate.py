def gridGenerator(n):
	with open("PixelPage.html", "w+") as f:
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write("<head>\n")
		f.write("\t<title>pDraw</title>\n")
		f.write("\t<link rel = \"stylesheet\" href = \"PixelPage.css\">\n")
		f.write("\t<script src=\"PixelPage.js\"></script>\n")
		f.write("</head>\n")
		f.write("<body>\n")
		f.write("\t<div class = \"grid\">\n")
		f.write("\t<ul class = row>\n")
		for i in range(n):
			if i != 0:
				f.write("\t<ul> \n")
			for i in range(n + 1):
				f.write("\t<li class = \"block\"> </li>\n")
			f.write("\t</ul>\n")
		f.write("\t</div>")
		f.write("\t<input type=\"color\" name=\"selectedColour\" value=\"#0000\">\n\t<input type="submit">\n")
		f.write("</body>\n")
		f.write("</html>")
gridGenerator(input())