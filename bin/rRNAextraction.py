#!/usr/bin/env python2
import os
import sys
def main():
	gff = sys.argv[1]
	ffn = sys.argv[2]
	Out = sys.argv[3]
	f = open(gff,"rb")
	data = f.readlines()
	f.close()
	Pool = []
	for each in data:
		if each[:-1] == "##FASTA":
			break
		if each[0] != "#":
			each = each[:-1]
			tmp = each.split("\t")
			if tmp[2] == "rRNA":
				tmp2 = tmp[8].split(";")
				Pool.append(tmp2[0][3:])
	flag = 0
	f = open(ffn,"rb")
	data = f.readlines()
	f.close()
	f = open(Out,"w")
	for each in data:
		if each[0] == ">":
			tmp = each.split(" ")
			if tmp[0][1:] in Pool:
				flag = 1
			else:
				flag = 0
		if flag == 1 and each[0] == ">":
			tmp = each.split(" ")
			f.writelines(["-".join(tmp)])
		elif flag == 1:
			f.writelines([each])
	f.close()
if __name__ == "__main__":
	main()
