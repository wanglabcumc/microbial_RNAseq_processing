#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	Out = sys.argv[2]
#	readsLen = float(sys.argv[3])
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	f = open(In + ".summary","rb")
	data2 = f.readlines()
	f.close()
	tmp = [int(e.split("\t")[1]) for e in data2[1:]]
	TotalMappedReads = tmp[0] + tmp[9] + tmp[11]
	TotalAssignedReads = tmp[0]

	T = 0
	for each in data[2:]:
		each = each[:-1]
		tmp = each.split("\t")
		genelen = int(tmp[5])
		count = int(tmp[6])
		T += count * 1.0 / genelen

	f = open(Out,"w")
	tmp = data[1].split("\t")
	f.writelines(["\t".join(tmp[:-1]) + "\tCount\tRPKM\tFPKMO\tTPM" + os.linesep])
	for each in data[2:]:
		each = each[:-1]
		tmp = each.split("\t")
		genelen = int(tmp[5])
		count = int(tmp[6])
		if TotalAssignedReads == 0:
			RPKM = 0
			FPKMO = 0
			TPM = 0
		else:
			RPKM = (10 ** 3) * (10 ** 6) * count * 1.0 / (TotalMappedReads * genelen)
			FPKMO = (10 ** 3) * (10 ** 6) * count * 1.0 / (TotalAssignedReads * genelen)
			TPM = (10 ** 6) * count * 1.0 / (T * genelen)
		f.writelines([each + "\t" + str(RPKM) + "\t" + str(FPKMO) + "\t" + str(TPM) + os.linesep])
	f.close()
if __name__ == "__main__":
	main()
