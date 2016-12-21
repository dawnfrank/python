import os

a = 2

class Base(object):
	pass

class Test(Base):
	def GetStr(self,a,b = 1,*c,**d):
		strList=[]
		for i in range(0,5,1):
			strList.append(str(i))
		else:
			print "strList:%s"%(strList)
		return os.path.join(strList)
			
	def IsTrue(self):
		if a:
			return True
		else:
			return False
	
	def testDict(self):
		global a
		b = {1:1,2:2}
		for key,_ in b.items():
			if key==1:
				continue
			else:
				break
		del b[1]
		
	def testAlgo(self):
		a = 1 + 2
		b = a - 3
		c = a*b
		d = a/b
		e = a %b
		f  = a^b
		g = a<<b
		h = a>>b
		j = [[a,b,c,d,e,f,g,h]]
		z = set(*j)
		return len(z)