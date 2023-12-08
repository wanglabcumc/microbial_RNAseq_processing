#!/usr/bin/env python
import os
import sys
def main():
    reads1 = sys.argv[1]
    reads2 = sys.argv[2]
    seq = sys.argv[3]
    f = open(reads1,"rb")
    fw = open(reads2,"w")
    qualityV = "A" * len(seq)
    for e in f:
        if e[0] == "@":
            tmp = e[:-1].split(" ")
            tmpO = tmp[0] + " 2" + tmp[1][1:]
            fw.writelines([tmpO + os.linesep])
            fw.writelines([seq + os.linesep])
            fw.writelines(["+" + os.linesep])
            fw.writelines([qualityV + os.linesep])
        else:
            continue
    f.close()
    fw.close()
if __name__ == "__main__":
    main()
