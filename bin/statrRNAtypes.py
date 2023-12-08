#!/usr/bin/env python
import os
import sys
def main():
    InSam = sys.argv[1]
    ref = sys.argv[2]
    Out = sys.argv[3]
    f = open(ref,"rb")
    data = f.readlines()
    f.close()
    Pool = {}
    for each in data:
        if each[0] == ">":
            Pool[each[1:-1]] = 0
    f = open(InSam,"rb")
    for each in f:
        if each[0] == "@":
            continue
        else:
            tmp = each.split("\t")
            if tmp[2] != "*":
                Pool[tmp[2]] += 1
    f.close()
    f = open(Out,"w")
    for each in Pool.keys():
        f.writelines([each + "\t" + str(Pool[each]) + os.linesep])
    f.close()
if __name__ == "__main__":
    main()
