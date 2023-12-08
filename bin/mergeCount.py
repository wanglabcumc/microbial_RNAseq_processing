#!/usr/bin/env python2
import os
import sys
def main():
	InFile = sys.argv[1]
	InDir = sys.argv[2]
	prefix = sys.argv[3]
	strain = sys.argv[4]
	Out = sys.argv[5]
	
	f = open(InFile,"rb")
	data = f.readlines()
	f.close()
	
	Pool = []
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		name = tmp[0]
		tmp2 = name.split("_")
		if tmp2[0] == strain:
			Pool.append(name)

	GenePool = []
	Exp = []
	f = open(InDir + "/" + prefix + "." + Pool[0] + ".featureCount.all.txt","rb")
	data = f.readlines()
	f.close()
	for each in data[2:]:
		each = each[:-1]
		tmp = each.split("\t")
		GenePool.append(tmp[:6])
		Exp.append([tmp[6]])

	for eachFile in Pool[1:]:
		f = open(InDir + "/" + prefix + "." + eachFile + ".featureCount.all.txt","rb")
		data = f.readlines()
		f.close()
		for i in range(2,len(data)):
			line = data[i][:-1]
			tmp = line.split("\t")
			Exp[i - 2].append(tmp[6])
	
	f = open(Out,"w")
	header = "#CommandLine" + os.linesep + "Geneid\tChr\tStart\tEnd\tStrand\tLength"
	for each in Pool:
		tmp = each.split("_")
		header += "\t" + each
	f.writelines([header + os.linesep])
	for i in range(len(Exp)):
		each = Exp[i]
		f.writelines(["\t".join(GenePool[i]) + "\t" + "\t".join(each) + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
