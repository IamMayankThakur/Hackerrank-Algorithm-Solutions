#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    m = 0
    for i in range(len(a)):
        c = 0
        for j in range(i,len(a)):
            if(abs(a[i]-a[j])<=1):
                c = c+1
        if(c>m):
               m = c
    return m
               
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
