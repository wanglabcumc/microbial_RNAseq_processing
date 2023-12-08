#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	Out = sys.argv[2]
	Prefix = sys.argv[3]
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	f = open(Out,"w")
	i = 0
	for each in data:
		if ">" == each[0]:
			f.writelines([">" + Prefix + "." + str(i) + os.linesep])
			i += 1
		else:
			f.writelines([each])
	f.close()
if __name__ == "__main__":
	main()
		
