#!/usr/bin/env python2
import os
import sys
basePool = {"A":"T","C":"G","T":"A","G":"C"}
def reverse(Seq):
	tmp = ""
	for e in Seq:
		tmp = basePool[e] + tmp
	return(tmp)

def main():
	In = sys.argv[1]
	Ada = sys.argv[2]
	Out = sys.argv[3]
	f = open(Ada,"rb")
	data = f.readlines()
	f.close()
	adPool = {}
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		tmp2 = tmp[0].split("_")
		adPool[tmp2[1]] = reverse(tmp[1][1:9])

	f = open(In,"rb")
	data = f.readlines()
	f.close()
	f = open(Out,"w")
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		Name = tmp[0] + "_" + tmp[1] + "_" + tmp[2] + "_" + tmp[3]
		adaSeq = adPool[tmp[5]]
		f.writelines([Name + "\t" + adaSeq + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
