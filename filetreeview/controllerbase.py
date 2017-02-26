# -*- coding:utf-8 -*-

from PyQt4 import QtCore

class CControllerBase(QtCore.QObject):
	def __init__(self,parent=None):
		super(CControllerBase,self).__init__(parent)
		self.initData()

	def initData(self):
		self.keys = []
		self.funcs = {}

	def RegisterHotKey(self,key,func,*param):
		self.funcs[key] = func,param
	
	def ReleaseHotKey(self,key):
		if key in self.funcs:
			del self.funcs[key]

	def mousePressEvent(self,event):
		if event.button() == QtCore.Qt.LeftButton:
			self.LeftDown(event)
		elif event.event() == QtCore.Qt.RightButton:
			self.RightDown(event)
	
	def mouseReleaseEvent(self,event):
		if event.button() == QtCore.Qt.LeftButton:
			self.LeftUp(event)
		elif event.button() == QtCore.Qt.RightButton:
			self.RightUp(event)

	def mouseDoubleClickEvent(self,event):
		if event.button() == QtCore.Qt.LeftButton:
			self.LeftDoubleClick(event)
		elif event.button() == QtCore.Qt.RightButton:
			self.RightDoubleClick(event)
	
	def keyPressEvent(self,event):
		key = event.key()
		self.keys.append(key)
		self._refresh(key)
	
	def keyReleaseEvent(self,event):
		key = event.key()
		if key in self.keys:
			self.keys.remove(event.key())
		
	def _refresh(self,key):
		for key in self.keys:
			if key in self.funcs:
				func,param = self.funcs[key]
				if param:
					func(*param)
				else:
					func()
		
	def LeftDown(self,event):
		pass
	
	def LeftUp(self,event):
		pass
	
	def RightDown(self,event):
		pass
	
	def RightUp(self,event):
		pass
	
	def LeftDoubleClick(self,event):
		pass
	
	def RightDoubleClick(self,event):
		pass