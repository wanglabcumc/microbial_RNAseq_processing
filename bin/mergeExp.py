#!/usr/bin/env python2
import os
import sys
def main():
	InFile = sys.argv[1]
	InDir = sys.argv[2]
	prefix = sys.argv[3]
	strain = sys.argv[4]
	Out = sys.argv[5]
	Type = sys.argv[6]
	
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

	if Type == "RPKM":
		bias = 7
	if Type == "FPKMO":
		bias = 8
	if Type == "TPM":
		bias = 9
	GenePool = []
	Exp = []
	f = open(InDir + "/" + prefix + "." + Pool[0] + ".all.exp","rb")
	data = f.readlines()
	f.close()
	for each in data[1:]:
		each = each[:-1]
		tmp = each.split("\t")
		GenePool.append(tmp[0])
		Exp.append([tmp[bias]])

	for eachFile in Pool[1:]:
		f = open(InDir + "/" + prefix + "." + eachFile + ".all.exp","rb")
		data = f.readlines()
		f.close()
		for i in range(1,len(data)):
			line = data[i][:-1]
			tmp = line.split("\t")
			Exp[i - 1].append(tmp[bias])
	
	f = open(Out,"w")
	header = "geneID"
	for each in Pool:
		tmp = each.split("_")
		header += "\t" + each
	f.writelines([header + os.linesep])
	for i in range(len(Exp)):
		each = Exp[i]
		f.writelines([GenePool[i] + "\t" + "\t".join(each) + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
