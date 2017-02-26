# -*- coding:utf-8 -*-  

from PIL import Image

im = Image.open("test.tga")
im.show()
print im.size
print im.getpixel((0,0))
print im.getpixel((549,0))
print im.getpixel((0,824))