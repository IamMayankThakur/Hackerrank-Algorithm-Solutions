#!/bin/python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if((ar[i]+ar[j])%k == 0):
                c = c +1 
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = map(int, raw_input().rstrip().split())

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()