#!/usr/bin/env python
import os
import sys
def main():
    In = sys.argv[1]
    Out = sys.argv[2]
    f = open(In,"rb")
    data = f.readlines()
    f.close()
    f = open(Out,"w")
    for i in range(len(data) / 4):
        f.writelines([str(len(data[4 * i + 1])) + os.linesep])
    f.close()
if __name__ == "__main__":
    main()
