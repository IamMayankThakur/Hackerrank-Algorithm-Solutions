#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    c = 0 
    for i in range(len(s)-m+1):
        su = 0
        for j in range(m):
            su = su + s[i+j]
        if(su == d):
            c = c + 1
    return c
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
