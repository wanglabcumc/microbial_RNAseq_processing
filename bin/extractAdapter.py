#!/usr/bin/env python
import os
import sys
def main():
    In = sys.argv[1]
    ref = sys.argv[2]
    out = sys.argv[3]
    f = open(In,"rb")
    data = f.readlines()
    f.close()
    Pool = {}
    for i in range(len(data) / 4):
        label = data[4 * i][:-1]
        seq = data[4 * i + 1][:-1]
        Pool[label] = seq
    f = open(ref,"rb")
    data = f.readlines()
    f.close()
    f = open(out,"w")
    for i in range(len(data) / 4):
        label = data[4 * i][:-1]
        seq = data[4 * i + 1][:-1]
        seqlen = len(seq) + 5
        rowSeq = Pool[label]
        adaptSeq = rowSeq[seqlen:]
        f.writelines([">" + label + os.linesep])
        f.writelines([adaptSeq + os.linesep])
    f.close()
if __name__ == "__main__":
    main()
