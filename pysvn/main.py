import svnfunc

TRUNK = "file:///G:/SVNLOCAL"
COMMIT = "file:///G:/SVNLOCAL1"

def main():
	svnfunc.SvnMergeInfo(COMMIT)

main()