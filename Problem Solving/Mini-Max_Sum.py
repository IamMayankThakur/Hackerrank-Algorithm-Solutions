#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sm = 0
    smin = 0
    for i in range(0,4):
        sm = sm + arr[len(arr)-(i+1)]
        smin = smin + arr[i]
    print(str(smin) +" "+ str(sm))




if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
