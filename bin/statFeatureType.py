#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	Pool = {}
	for each in data:
		if each[0] == ">":
			break	
		if each[0] != "#":
			tmp = each.split("\t")
			Pool[tmp[2]] = 0
	for each in data:
		if each[0] == ">":
			break
		if each[0] != "#":
			tmp = each.split("\t")
			Pool[tmp[2]] += 1
	for each in Pool.keys():
		print each + "\t" + str(Pool[each])
if __name__ == "__main__":
	main()


