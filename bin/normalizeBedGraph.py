#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	Stat = sys.argv[2]
	Out = sys.argv[3]
	f = open(Stat,"rb")
	data = f.readlines()
	f.close()
	tmp = data[0][:-1].split(" ")
	TotalReads = int(tmp[-1])
	factors = TotalReads / 1000000.0
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	f = open(Out,"w")
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		chrN = tmp[0]
		start = tmp[1]
		end = tmp[2]
		value = float(tmp[3]) / factors
		f.writelines([chrN + "\t" + start + "\t" + end + "\t" + str(value) + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
