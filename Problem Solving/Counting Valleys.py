#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    k = list()
    for i in s:
        if(i=="U"):
            k.append(1)
        else:
            k.append(-1)
    s = 0
    c = 0
    f = 1
    for i in k:
        if(s < 0 and f):
            c = c +1 
            f = 0
        if(s>=0):
            f = 1 
        s = s + i
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()