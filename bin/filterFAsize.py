#!/usr/bin/env python
import os
import sys
def main():
    In = sys.argv[1]
    Out = sys.argv[2]
    cutoff = int(sys.argv[3])
    f = open(In,"rb")
    fw = open(Out,"w")
    for each in f:
        if each[0] != ">":
            seq = each[:-1]
            if len(seq) >= cutoff:
                fw.writelines([seq + os.linesep])
    f.close()
    fw.close()
if __name__ == "__main__":
    main()
