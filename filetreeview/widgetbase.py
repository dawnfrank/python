# -*- coding:utf-8 -*-

from PyQt4 import QtGui

class CWidgetBase(QtGui.QTreeView):
	def __init__(self,parent=None):
		super(CWidgetBase,self).__init__(parent)
		
		self._controllerObj = None
	
	def _bindController(self,ctrlObj):
		self._controllerObj = ctrlObj

	def mousePressEvent(self,event):
		QtGui.QTreeView.mousePressEvent(self,event)
		self._controllerObj.mousePressEvent(event)

	def mouseReleaseEvent(self,event):
		QtGui.QTreeView.mouseReleaseEvent(self,event)
		self._controllerObj.mouseReleaseEvent(event)
			
		
	def keyPressEvent(self,event):
		QtGui.QTreeView.keyPressEvent(self,event)
		self._controllerObj.keyPressEvent(event)
			
	def keyReleaseEvent(self,event):
		QtGui.QTreeView.keyReleaseEvent(self,event)
		self._controllerObj.keyReleaseEvent(event)
			
		
	def mouseDoubleClickEvent(self,event):
		QtGui.QTreeView.mouseDoubleClickEvent(self,event)
		self._controllerObj.mouseDoubleClickEvent(event)

"""	
	def mousePressEvent(self,event):
		if self._controllerObj:
			self._controllerObj.mousePressEvent(event)
		else:
			QtGui.QWidget.mousePressEvent(self,event)
		
	def mouseReleaseEvent(self,event):
		if self._controllerObj:
			self._controllerObj.mouseReleaseEvent(event)
		else:
			QtGui.QWidget.mouseReleaseEvent(self,event)
		
	def keyPressEvent(self,event):
		if self._controllerObj:
			self._controllerObj.keyPressEvent(event)
		else:
			QtGui.QWidget.keyPressEvent(self,event)
		
	def keyReleaseEvent(self,event):
		if self._controllerObj:
			self._controllerObj.keyReleaseEvent(event)
		else:
			QtGui.QWidget.keyReleaseEvent(self,event)
		
	def mouseDoubleClickEvent(self,event):
		if self._controllerObj:
			self._controllerObj.mouseDoubleClickEvent(event)
		else:
			QtGui.QWidget.mouseDoubleClickEvent(self,event)
"""