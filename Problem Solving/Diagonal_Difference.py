#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    ltr = 0
    rtl = 0
    print(arr)
    for i in range(0,len(arr)):
        ltr = ltr + arr[i][i]
        rtl = rtl + arr[i][len(arr)-(i+1)]
    print(ltr)
    print(rtl)
    if(ltr - rtl < 0 ):
        return((ltr-rtl)*-1)
    else:
        return((ltr-rtl))




        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()