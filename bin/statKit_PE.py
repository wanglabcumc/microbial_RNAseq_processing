#!/usr/bin/env python2
import os
import sys
def statTotalReads(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".N_filter.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[8][:-1]
		tmp2 = tmp.split(" ")
		tmp3 = tmp2[-1].split(",")
		tmpPool.append(int("".join(tmp3)))
	for each in tmpPool:
		print each
def statNremoval(Indir,SampleList):	
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".N_filter.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[11][:-1]
		tmp2 = tmp.split(" ")
		tmp3 = tmp2[-2].split(",")
		tmpPool.append(int("".join(tmp3)))
	for each in tmpPool:
		print each
def statPhiXremoval(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".phiX_filter.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[3][:-1]
		tmp2 = tmp.split("(")
		num1 = int(tmp2[0])
		tmp = data[4][:-1]
		tmp2 = tmp.split("(")
		num2 = int(tmp2[0])
		tmp = data[12][:-1]
		tmp2 = tmp.split("(")
		num3 = int(tmp2[0])
		tmp = data[13][:-1]
		tmp2 = tmp.split("(")
		num4 = int(tmp2[0])
		tmpPool.append(num1 + num2 + num3 + num4)
	for each in tmpPool:
		print each
def statpolyG(Indir,SampleList):	
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".polyG_filter.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[12][:-1]
		tmp2 = tmp.split(" ")
		tmp3 = tmp2[-2].split(",")
		num1 = int("".join(tmp3))
		tmp = data[8][:-1]
		tmp2 = tmp.split(" ")
		tmp3 = tmp2[-1].split(",")
		num2 = int("".join(tmp3))
		tmpPool.append(num2 - num1)
	for each in tmpPool:
		print each

def statQC(Indir,SampleList):	
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".adapter_remove_QC_second.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[16][:-1]
		tmp2 = tmp.split(" ")
		tmp3 = tmp2[-2].split(",")
		tmpPool.append(int("".join(tmp3)))
	for each in tmpPool:
		print each
def statrRNA(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".rRNA_filter.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[3][:-1]
		tmp2 = tmp.split("(")
		num1 = int(tmp2[0])
		tmp = data[4][:-1]
		tmp2 = tmp.split("(")
		num2 = int(tmp2[0])
		tmp = data[12][:-1]
		tmp2 = tmp.split("(")
		num3 = int(tmp2[0])
		tmp = data[13][:-1]
		tmp2 = tmp.split("(")
		num4 = int(tmp2[0])
		tmpPool.append(num1 + num2 + num3 + num4)
	for each in tmpPool:
		print each
def statGenome(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".map.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[-1][:-1]
		tmp2 = tmp.split(" ")
		tmpPool.append(int(tmp2[1]))
	for each in tmpPool:
		print each
def statPCRdup(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/" + each + ".PCRdup.log","rb")
		data = f.readlines()
		f.close()
		tmp = data[1][:-1]
		tmp2 = tmp.split(" ")
		tmpPool.append(int(tmp2[-1]) / 2)
	for each in tmpPool:
		print each
def statCDS(Indir,SampleList):
	tmpPool = []
	for each in SampleList:
		f = open(Indir + "/RNAScreen1." + each + ".featureCount.all.txt.summary","rb")
		data = f.readlines()
		f.close()
		tmp = data[1][:-1]
		tmp2 = tmp.split("\t")
		tmpPool.append(int(tmp2[-1]))
	for each in tmpPool:
		print each
def main():
	Indir = sys.argv[1]
	SampleFile = sys.argv[2]
	Item = sys.argv[3]
	f = open(Indir + "/" + SampleFile,"rb")
	data = f.readlines()
	f.close()
	SampleList = []
	for each in data:
		each = each[:-1]
		tmp = each.split("\t")
		SampleList.append(tmp[0])
	if Item == "total":
		statTotalReads(Indir + "/1.phixRemove",SampleList)
	if Item == "N":
		statNremoval(Indir + "/1.phixRemove",SampleList)
	if Item == "phiX":
		statPhiXremoval(Indir + "/1.phixRemove",SampleList)
	if Item == "polyG":
		statpolyG(Indir + "/2.adatperTrimAndQC",SampleList)
	if Item == "QC":
		statQC(Indir + "/2.adatperTrimAndQC",SampleList)
	if Item == "rRNA":
		statrRNA(Indir + "/3.rRNAremoval",SampleList)
	if Item == "genome":
		statGenome(Indir + "/4.bowtieMap",SampleList)
	if Item == "PCRdup":
		statPCRdup(Indir + "/4.bowtieMap",SampleList)
	if Item == "CDS":
		statCDS(Indir + "/6.expresssion/count",SampleList)
if __name__ == "__main__":
	main()
