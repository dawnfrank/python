# -*- coding:utf-8 -*-  

import time
import sys
from PyQt4 import QtGui

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