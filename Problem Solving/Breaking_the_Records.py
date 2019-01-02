#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minVal = scores[0]
    minC = 0
    maxVal = scores[0]
    maxC = 0
    for i in scores:
        if(i > maxVal):
            maxVal = i
            maxC = maxC +1
        elif(i<minVal):
            minVal = i
            minC = minC + 1 
    l = list()
    l.append(str(maxC))
    l.append(str(minC))
    return l



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
