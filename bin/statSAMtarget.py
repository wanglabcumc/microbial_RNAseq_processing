#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	f = open(In,"rb")
	Pool = {}
	for each in f:
		if each[0] != "@":
			tmp = each.split("\t")
			if tmp[2] not in Pool.keys():
				Pool[tmp[2]] = 1
			else:
				Pool[tmp[2]] += 1
	f.close()
	for each in Pool.keys():
		print each + "\t" + str(Pool[each])
if __name__ == "__main__":
	main()
