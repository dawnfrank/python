# -*- coding:utf-8 -*-

import filedata
import controllerbase
	
from PyQt4 import QtCore


class CFileWidgetCtrl(controllerbase.CControllerBase):
	def __init__(self,parent=None):
		super(CFileWidgetCtrl,self).__init__(parent)

		self.RegisterHotKey(QtCore.Qt.Key_Up, self.OnKeyUp)
		self.RegisterHotKey(QtCore.Qt.Key_Up, self.OnKeyDown)
		
	def OnKeyUp(self):
		nextIndex = self.parent().indexAbove(self.parent().currentIndex())
		filedata.GetFileData().currFile = nextIndex

	def OnKeyDown(self):
		nextIndex = self.parent().indexBelow(self.parent().currentIndex())
		filedata.GetFileData().currFile = nextIndex

	def LeftDown(self,event):
		modelIndex = self.parent().indexAt(event.pos())
		filedata.GetFileData().currFile = modelIndex
		filedata.GetFileData().currDir = modelIndex

	def LeftDoubleClick(self, event):
		pass
#		modelIndex = self.parent().indexAt(event.pos())
#		if filedata.GetFileModel().isDir(modelIndex):
#			filedata.GetFileData().currDir = modelIndex

