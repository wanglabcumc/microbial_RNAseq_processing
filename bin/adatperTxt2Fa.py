#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	Out = sys.argv[2]
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	f = open(Out,"w")
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		tmp2 = tmp[0].split("_")
		f.writelines([">" + tmp2[1] + os.linesep])
		f.writelines([tmp[1] + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
