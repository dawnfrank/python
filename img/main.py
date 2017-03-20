# -*- coding:utf-8 -*-  

import sys
import _binary
from PIL import Image
from PyQt4 import QtGui

o8 = _binary.o8
o16 = _binary.o16le
o32 = _binary.o32le

class CImageData(object):
	def __init__(self):
		self.datas = {}
		self.size=0,0
		self.bytes = 0
		self.tgaType= 0
		
	def SetInfo(self,data,size,tgaBytes,tgaType):
		self.datas = data
		self.size = size
		self.bytes = tgaBytes
		self.tgaType = tgaType
		
g_Data = CImageData()

def GetImagData():
	global g_Data
	return g_Data

def mirror(data,width):
	newData = {}
	for index,color in data.iteritems():
		row = index / width
		col = index % width
		index = (width - row -1)*width + col
		newData[index] = color
	return newData

def LoadTga(path):
	global g_Data
	with open(path,"rb") as f:
		header = f.read(18)
		additionLen =  ord(header[0])
		f.seek(18+additionLen)
		fdatas = f.read()
		f.close()

		tgaType = ord(header[2])
		width = ord(header[13])*256+ord(header[12])
		height = ord(header[15])*256+ord(header[14])
		imBytes = ord(header[16])
		isMirror = imBytes != 0xf

		data = {}
		
		if tgaType == 2:
			for i in xrange(height):
				for j in xrange(width):
					num = i*width + j
					data[num] = fdatas[num*4:(num+1)*4]
		elif tgaType == 10:	#RLE
			isRepeat = False
			repeatNum = 0
			colorStr = ""
			while i<height*width:
				if not repeatNum:
					isRepeat = fdatas[0] >> 7
					repeatNum = fdatas[0] & 0x7f + 1
					colorStr = ""
					fdatas = fdatas[1:]
					continue
				elif isRepeat:
					if colorStr:
						colorStr = fdatas[:4]
						fdatas = fdatas[4:]
					data[i] = colorStr
					repeatNum -= 1
				else:
					data[i] = fdatas[:4]
					fdatas = fdatas[4:]
					repeatNum -= 1
				i+=1
					
		if isMirror:
			data = mirror(data, width)

		g_Data.SetInfo(data,(width,height),imBytes,tgaType)


def SaveTga(dstPath):
	global g_Data
	tgaData = g_Data
	isMirror = tgaData.bytes != 0xf
	dataList = []
	width = tgaData.size[0]
	
	datas = tgaData.datas
	if isMirror:
		datas = mirror(datas, width)
	
	for index,color in datas.iteritems():
		dataList.append([index,color])
	dataList.sort()
	dataList = [i[1] for i in dataList]
	data = "".join(dataList)

	with open(dstPath,"w") as f:
		f.write(o8(0))
		f.write(o8(0))
		f.write(o8(tgaData.tgaType))
		f.write(o16(0))
		f.write(o16(0))
		f.write(o8(0))
		f.write(o16(0))
		f.write(o16(0))
		f.write(o16(tgaData.size[0]))
		f.write(o16(tgaData.size[1]))
		f.write(o8(tgaData.bytes))
		f.write(o8(8))
		f.write(data)

class CWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(CWidget,self).__init__(parent)
		
		self.initData()

	def initData(self):
		LoadTga(srcPath)
		
		global g_Data
		tgaData = g_Data
		datas = tgaData.datas
		dataList = []
		width,height = tgaData.size
		for index,color in datas.iteritems():
			dataList.append([index,color])
		dataList.sort()
		dataList = [i[1] for i in dataList]
		data = "".join(dataList)

		with open("test2.tga","w") as f:
			f.write(o8(0))
			f.write(o8(0))
			f.write(o8(tgaData.tgaType))
			f.write(o16(0))
			f.write(o16(0))
			f.write(o8(0))
			f.write(o16(0))
			f.write(o16(0))
			f.write(o16(tgaData.size[0]))
			f.write(o16(tgaData.size[1]))
			f.write(o8(tgaData.bytes))
			f.write(o8(8))
			f.write(data)

		image = QtGui.QImage(data,width,height,QtGui.QImage.Format_ARGB32)
		pixmap = QtGui.QPixmap.fromImage(image)
		
		self.resize(width,height)
		self.label = QtGui.QLabel(self)
		self.label.setPixmap(pixmap)
		
	def initData1(self):
		fp = open("test1.tga","rb")
		header = fp.read(18)
		width = ord(header[13])*256+ord(header[12])
		height = ord(header[15])*256+ord(header[14])
	
		datas = fp.read()
		image = QtGui.QImage(datas,width,height,QtGui.QImage.Format_ARGB32)
		image = image.mirrored(False, True)
		pixmap = QtGui.QPixmap.fromImage(image)
		self.resize(pixmap.size())
		
		self.label = QtGui.QLabel(self)
		self.label.setPixmap(pixmap)


srcPath = "test.tga"
dstPath = "test1.tga"

if __name__ == "__main__":
#	LoadTga(srcPath)
#	SaveTga(dstPath)
#	im = Image.open("test1.tga")
#	im.show()


	app = QtGui.QApplication([])
	widget = CWidget()
	widget.show()
	widget.setMinimumSize(200, 200)
	sys.exit(app.exec_())

"""
class CWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(CWidget,self).__init__(parent)
		
		self.initData()

	def initData(self):
		fp = open("test.tga","rb")
		header = fp.read(18)
		width = ord(header[13])*256+ord(header[12])
		height = ord(header[15])*256+ord(header[14])
		imBytes = ord(header[16]) >> 3
		imgSize = width*height * imBytes

		datas = fp.read()
		image = QtGui.QImage(datas,width,height,QtGui.QImage.Format_ARGB32)
		image = image.mirrored(False, True)
		pixmap = QtGui.QPixmap.fromImage(image)
		self.resize(pixmap.size())
		
		self.label = QtGui.QLabel(self)
		self.label.setPixmap(pixmap)

if __name__ == "__main__":
	app = QtGui.QApplication([])
	widget = CWidget()
	widget.show()
	sys.exit(app.exec_())
"""