#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    c = len(arr)
    l = list()
    while(c>0):
        m = min(arr)
        l.append(c)
        for i in range(len(arr)):
            arr[i] = arr[i]-m
            if(arr[i]<=0):
                arr[i] = 20000000
                c = c-1
    return l
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
