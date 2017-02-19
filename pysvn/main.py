import svnfunc

TRUNK = "file:///G:/SVNLOCAL/trunk"
COMMIT = "file:///G:/SVNLOCAL/branch"
LOCAL = "G:/SVNTEST/branch"

def GetSVNMergeInfo(source,target):
	svnfunc.SvnMergeInfo(source,target)

def main():
	GetSVNMergeInfo(TRUNK,LOCAL)

main()