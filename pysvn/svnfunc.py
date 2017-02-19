import subprocess
import misc

def SvnLog(path):
	commondStr = "svn log %s"%path
	resStr = subprocess.check_output(commondStr,shell = True)
	print resStr
	
def SvnMergeInfo(source,target):
	commondStr = "svn mergeinfo --show-revs=eligible %s %s"%(source,target)
	resStr = subprocess.Popen(commondStr,shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout,stderror=resStr.communicate()
	if stderror:
		pass
	verIDList = stdout.split(misc.GetLineSep())
	print verIDList