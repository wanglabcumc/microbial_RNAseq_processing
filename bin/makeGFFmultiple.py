#!/usr/bin/env python2
import os
import sys
UTR3 = 250
UTR5 = 10 
def main():
	In = sys.argv[1]
	Out = sys.argv[2]
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	Pool = []
	frRNA = open(Out + ".rRNA.bed","w")
	fmRNA = open(Out + ".mRNA.bed","w")
	ftRNA = open(Out + ".tRNA.bed","w")
	frepeat = open(Out + ".repeat.bed","w")
	for each in data:
		if each[0] == ">":
			break
		if each[0] == "#":
			continue
		else:
			each = each[:-1]
			tmp = each.split("\t")
			start = int(tmp[3]) - 1
			end = int(tmp[4])
			chrN = tmp[0]
			if tmp[2] == "rRNA":
				frRNA.writelines([chrN + "\t" + str(start) + "\t" + str(end) + "\t" + tmp[8] + "\t.\t" + tmp[6] + os.linesep])
			elif tmp[2] == "CDS":
				if tmp[6] == "+":
					fmRNA.writelines([chrN + "\t" + str(max(start - UTR5,1)) + "\t" + str(end + UTR3) + "\t" + tmp[8] + "\t.\t" + tmp[6] + os.linesep])
				else:
					fmRNA.writelines([chrN + "\t" + str(max(start - UTR3,1)) + "\t" + str(end + UTR5) + "\t" + tmp[8] + "\t.\t" + tmp[6] + os.linesep])
			elif tmp[2] == "tRNA":
				ftRNA.writelines([chrN + "\t" + str(start) + "\t" + str(end) + "\t" + tmp[8] + "\t.\t" + tmp[6] + os.linesep])
			elif tmp[2] == "repeat_region":
				frepeat.writelines([chrN + "\t" + str(start) + "\t" + str(end) + "\t" + tmp[8] + "\t.\t" + tmp[6] + os.linesep])
	frRNA.close()
	fmRNA.close()
	ftRNA.close()
	frepeat.close()
if __name__ == "__main__":
	main()
