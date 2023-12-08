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
	Pool = []
	for each in data:
		each = each[:-1]
		Pool.append(each.split("\t"))
	f = open(Out,"w")
	for each in Pool:
		f.writelines([each[1] + " " + Prefix + "." + each[0] + ".R2.fq " + Prefix + "." + each[0] + ".R1.fq" + os.linesep])
	f.close()
if __name__ == "__main__":
	main()

