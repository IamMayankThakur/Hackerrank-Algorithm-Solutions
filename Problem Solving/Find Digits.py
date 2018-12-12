#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    l = list()
    c = 0
    k = str(n)
    for i in k:
        l.append(int(i))
    for j in l:
        if(j!= 0):
            if(n%j == 0):
                c = c+1
    return c
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
