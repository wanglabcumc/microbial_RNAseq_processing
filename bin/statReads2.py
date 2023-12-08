#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	f = open(In,"rb")
	Pool = {}
	for count, line in enumerate(f, start = 0):
		if count % 4 == 1:
			Pool[line[:-1]] = 0
	f.close()
	f = open(In,"rb")
	for count, line in enumerate(f, start = 0):
		if count % 4 == 1:
			Pool[line[:-1]] += 1
	Pool2 = []
	for each in Pool.keys():
		Pool2.append([Pool[each],each])
	Pool2.sort()
	for each in Pool2:
		print str(each[0]) + "\t" + each[1]
	f.close()
if __name__ == "__main__":
	main()


