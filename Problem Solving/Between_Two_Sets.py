#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    a.sort()
    b.sort()
    c = 0
    for i in range(a[len(a)-1],b[0]+1):
        f = 1
        for j in a:
            if(i % j !=0):
                f = 0
        for k in b:
            if(k % i != 0 ):
                f = 0
        if(f):
            c = c+1 
    return c




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
