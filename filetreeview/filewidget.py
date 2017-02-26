# -*- coding:utf-8 -*-

import sys

import filedata
import filewidgetctrl
import widgetbase

import signalmgr
import signaldefine
from PyQt4 import QtGui,QtCore

class CTreeView(widgetbase.CWidgetBase):
	def __init__(self,parent=None):
		super(CTreeView,self).__init__(parent)
		
		self.initData()
		self.initConnect()
		
		print dir(self)

	def initData(self):
		self.model = filedata.GetFileModel()
		self.setModel(self.model)
		
		self.setColumnHidden(1,True)
		self.setColumnHidden(2,True)
		self.setColumnHidden(3,True)
		self.header().hide()
		
		widgetCtrl = filewidgetctrl.CFileWidgetCtrl(self)
		self._bindController(widgetCtrl)

	def initConnect(self):
		self.connect(self,QtCore.SIGNAL("expanded(QModelIndex)"),self.CheckExpand)

		self.connect(signalmgr.GetSignalMgr(),signaldefine.SIGNAL_CURRFILE_INDEX,self.OnFilldataCurrentFileIndex)
		self.connect(signalmgr.GetSignalMgr(),signaldefine.SIGNAL_CURRDIR_INDEX,self.OnFilldataCurrentDirIndex)

	def CheckExpand(self,modelIndex):
		filePath = filedata.GetFileModel().filePath(modelIndex)
		for fileInfo in QtCore.QDir(filePath).entryInfoList(QtCore.QDir.AllDirs|QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot):
#			filePath = fileInfo.filePath()
#			if fileInfo.isDir() and len(QtCore.QDir(filePath).entryInfoList(QtCore.QDir.AllDirs|QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)) == 0:
#				modelIndex  = filedata.GetFileModel().index(filePath)
#				self.setRootIsDecorated(False)
			self.setItemsExpandable(False)

	def OnFilldataCurrentFileIndex(self,modelIndex):
		if modelIndex != self.currentIndex():
			self.setCurrentIndex(modelIndex)
		
	def OnFilldataCurrentDirIndex(self,modelIndex):
		self._expand(modelIndex)
		
	def expand(self,modelIndex):
		print modelIndex
		
	def _expand(self,modelIndex):
		model = filedata.GetFileModel()
		if self.isExpanded(modelIndex):
			self.setExpanded(modelIndex,False)
		else:
			while(model.filePath(modelIndex)):
				self.setExpanded(modelIndex,True)
				modelIndex = modelIndex.parent()
				
class CWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(CWidget,self).__init__(parent)

		self.initWidget()

	def initWidget(self):
		self.setMinimumSize(1024,768)
		self.treeView = CTreeView(self)
		self.treeView.resize(self.size())

if __name__ == "__main__":
	app = QtGui.QApplication([])
	widget = CWidget()
	widget.show()
	sys.exit(app.exec_())