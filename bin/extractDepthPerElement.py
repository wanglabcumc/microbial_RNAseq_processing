#!/usr/bin/env python
import os
import sys
def main():
    In = sys.argv[1]
    bed = sys.argv[2]
    chromSize = sys.argv[3]
    Out = sys.argv[4]
    f = open(chromSize,"rb")
    data = f.readlines()
    f.close()
    sizePool = {}
    for each in data:
        each = each[:-1]
        tmp = each.split("\t")
        sizePool[tmp[0]] = int(tmp[1])
    f = open(In,"rb")
    Pool = {}
    for each in f:
        each = each[:-1]
        tmp = each.split("\t")
        Pool[tmp[0] + "_" + tmp[1]] = tmp[2]
    f.close()
    f = open(bed,"rb")
    data = f.readlines()
    f.close()
    f = open(Out,"w")
    for each in data:
        each = each[:-1]
        tmp = each.split("\t")
        chrN = tmp[0]
        start = int(tmp[1]) + 1
        end = int(tmp[2])
        length = end - start + 1
        strand = tmp[5]
        tmp2 = tmp[3].split(";")
        tmpPool = {}
        for e in tmp2:
            tmp3 = e.split("=")
            tmpPool[tmp3[0]] = tmp3[1]
        ID = tmpPool["ID"]
        if start < 0 or end > sizePool[chrN]:
            continue
        value = ""
        if strand == "+":
            for i in range(start, end + 1):
                value = value + "," + Pool[chrN + "_" + str(i)]
            value = value[1:]
        else:
            for i in range(start, end + 1):
                value = Pool[chrN + "_" + str(i)] + "," + value
            value = value[:-1]
        f.writelines([ID + "\t" + str(start) + "\t" + str(end) + "\t" + strand + "\t" + str(length) + "\t" + value + os.linesep])
    f.close()
if __name__ == "__main__":
    main()
