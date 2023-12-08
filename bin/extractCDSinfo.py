#!/usr/bin/env python2
import os
import sys 
def main():
    In = sys.argv[1]
    Out = sys.argv[2]
    f = open(In,"rb")
    data = f.readlines()
    f.close()
    f = open(Out,"w")
    f.writelines(["id\tchrN\tstart\tend\tlength\tstrand\tgene\tproduct" + os.linesep])
    for each in data:
        each = each[:-1]
        if each[0] == "#":
            continue
        if each[0] == ">":
            break
        tmp = each.split("\t")
        if tmp[2] == "CDS":
            chrN = tmp[0]
            start = tmp[3]
            end = tmp[4]
            length = str(int(end) - int(start) + 1)
            strand = tmp[6]
            tmpPool = {}
            for each in tmp[8].split(";"):
                tmp2 = each.split("=")
                tmpPool[tmp2[0]] = tmp2[1]
            if "gene" in tmpPool.keys():
                gene = tmpPool["gene"]
            else:
                tmp3 = tmpPool["ID"].split("_")
                gene = "unknown" + "_" + tmp3[1]
            f.writelines([tmpPool["ID"] + "\t" + chrN + "\t" + start + "\t" + end + "\t" + length \
                        + "\t" + strand + "\t" + gene + "\t" + tmpPool["product"] + os.linesep])
    f.close()
if __name__ == "__main__":
    main()
