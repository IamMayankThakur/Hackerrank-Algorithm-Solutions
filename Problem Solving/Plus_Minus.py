#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0.000000
    n = 0.000000
    z = 0.000000
    for i in arr:
        if(i == 0):
            z = z+1
        elif(i<0):
            n = n + 1
        else:
            p = p + 1 
    l = float(len(arr))
    print("%.6f" %float(p/l))
    print(float(n/l))
    print(float(z/l))
if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
