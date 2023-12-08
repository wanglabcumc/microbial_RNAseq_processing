#!/usr/bin/env python2
import os
import sys
def main():
	In = sys.argv[1]
	Out = sys.argv[2]
	f = open(In,"rb")
	data = f.readlines()
	f.close()
	Pool = {}
	for i in range(len(data) / 4):
		Pool[data[4 * i]] = data[4 * i + 1] + data[4 * i + 2] + data[4 * i + 3]
	f = open(Out,"w")
	tmp = Pool.keys()
	tmp.sort()
	for each in tmp:
		f.writelines([each + Pool[each]])
	f.close()
if __name__ == "__main__":
	main()
