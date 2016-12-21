import os

def SvnLog(path):
	commondStr = "svn log %s"%path
	os.system(commondStr)
	
def SvnMergeInfo(path):
	commondStr = "svn mergeinfo %s"%path
	os.system(commondStr)