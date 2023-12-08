#!/usr/bin/env python2
import os
import sys
import threading
import time
threshold = 100000000
def subprocess(Read1,Read2,OutRead2):
	f2 = open(Read2,"rb")
	Pool = {}
	for count, line in enumerate(f2, start = 0):
		if count % 4 == 0:
			tmp = line.split(" ")
			tmp2 = tmp[0].split(":")
			Pool[":".join(tmp2[3:7])] = 0
#			Pool[tmp[0]] = 0 
	f2.close()

	f1 = open(Read1,"rb")
	for count, line in enumerate(f1, start = 0):
		if count % 4 == 0:
			tmp = line.split(" ")
			tmp2 = tmp[0].split(":")
			Pool[":".join(tmp2[3:7])] = 1
#			Pool[tmp[0]] = 1
	f2 = open(Read2,"rb")
	fw = open(OutRead2,"w")
	flag = 0
	for count, line in enumerate(f2, start = 0):
		if count % 4 == 0:
			tmp = line.split(" ")
			tmp2 = tmp[0].split(":")
			if Pool[":".join(tmp2[3:7])] == 0:
#			if Pool[tmp[0]] == 0:
				flag = 0
			else:
				flag = 1
		if flag == 1:
			fw.writelines([line])
			
	fw.close()
	f2.close()

def main():
	read1 = sys.argv[1]
	read2 = sys.argv[2]
	outRead2 = sys.argv[3]
#	core = int(sys.argv[4])
	f = open(read2,"rb")
	fw = open(outRead2 + ".tmp0","w")
	index = 0
	for count, line in enumerate(f, start = 0):
		if count % threshold == 0:
			fw.close()
			fw = open(outRead2 + ".tmp" + str(index),"w")
			index += 1
			fw.writelines([line])
		else:
			fw.writelines([line])
	fw.close()  
#	index = 13
	for i in range(index):
		print "file:\t" + str(i)
		subprocess(read1,outRead2 + ".tmp" + str(i),outRead2 + ".ftmp" + str(i))

	os.system("rm -f " + outRead2)
	for i in range(index):
		os.system("more " + outRead2 + ".ftmp" + str(i) + ">> " + outRead2)
		os.system("rm -f " + outRead2 + ".ftmp" + str(i))
		os.system("rm -f " + outRead2 + ".tmp" + str(i))


if __name__ == "__main__":
	main()
	
