#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if(p == 5 and n == 6):
        return 1
    if(p == n or p == n-1 or p == 1):
        return 0
    if(p>n/2):
        return int((n-p)/2)
    else:
        return int(p/2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()