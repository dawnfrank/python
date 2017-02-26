# -*- coding:utf-8 -*

import signalmgr
import signaldefine
from PyQt4 import QtGui

def GetFileData():
	return g_FileData

def GetFileModel():
	return g_FileData.model

class CFileData(object):
	def __init__(self):
		self.initData()
		
	def initData(self):
		self.fileModle = QtGui.QFileSystemModel()
		self.fileModle.setRootPath("")
		
		self.currFileIndex = None
		self.currDirIndex = None
		
	@property
	def model(self):
		return self.fileModle
		
	@property
	def currFile(self):
		return self.currFileIndex
	
	@currFile.setter
	def currFile(self,val):
		if val == self.currFileIndex:
			return
		self.currFileIndex = val
		signalmgr.emit(signaldefine.SIGNAL_CURRFILE_INDEX,val)

	@property
	def currDir(self):
		return self.currDirIndex
	
	@currDir.setter
	def currDir(self,val):
		if val == self.currDirIndex:
			return
		self.currDirIndex = val
		signalmgr.emit(signaldefine.SIGNAL_CURRDIR_INDEX,val)
		

g_FileData = CFileData()