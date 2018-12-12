#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    l = [0,0,0,0,0]
    l[0] = arr.count(1)
    l[1] = arr.count(2)
    l[2] = arr.count(3)
    l[3] = arr.count(4)
    l[4] = arr.count(5)
    maxV = l[0]
    maxPos = 1
    for i in range(1,len(l)):
        if(l[i]>maxV):
            maxPos = i+1
            maxV = l[i]
        
    return maxPos
            
        
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
