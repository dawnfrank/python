# -*- coding:utf-8 -*

from PyQt4 import QtCore

class CSignalMgr(QtCore.QObject):
	def __init__(self,parent=None):
		super(CSignalMgr,self).__init__(parent)
		
	def emitSignal(self,key,*param):
		if param:
			self.emit(key,*param)
		else:
			self.emit(key)
		
g_SignalMgr = CSignalMgr()

def GetSignalMgr():
	return g_SignalMgr

def emit(key,*param):
	g_SignalMgr.emitSignal(key,*param)