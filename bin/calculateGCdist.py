#!/usr/bin/env python
import os
import sys
baseList = ["G","C","T","A"]
def calGCvalue(seq):
    tmpPool = {}
    for e in baseList:
        tmpPool[e] = 0
    for e in seq:
        tmpPool[e] += 1
    return 1.0 * (tmpPool["G"] + tmpPool["C"]) / len(seq)
def calGCdist(seq):
    tmpPool = []
    for i in range(50, (len(seq) - 51)):
        position = i
        start = i - 50
        end = i + 50
        subSeq = seq[start:(end + 1)]
        tmpPool.append([position, position + 1, calGCvalue(subSeq)])
    return tmpPool
def main():
    In = sys.argv[1]
    Out = sys.argv[2]
    f = open(In,"rb")
    data = f.readlines()
    f.close()
    Pool = {}
    flag = 0
    tmpName = ""
    tmpSeq = ""
    for each in data:
        each = each[:-1]
        if each[0] == ">":
            Pool[tmpName] = tmpSeq
            tmpName = each[1:]
            tmpSeq = ""
        else:
            tmpSeq += each
        flag = 0
    Pool[tmpName] = tmpSeq
    f = open(Out,"w")
    for chrN in Pool.keys():
        tmpPool = calGCdist(Pool[chrN])
        for e in tmpPool:
            f.writelines([chrN + "\t" + "\t".join([str(p) for p in e]) + os.linesep])
    f.close()

if __name__ == "__main__":
    main()
