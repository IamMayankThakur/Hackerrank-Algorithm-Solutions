#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = int(n/len(s))
    li = list()
    c = 0
    for i in range(len(s)):
        if(s[i] == "a"):
            li.append(i)
    c = l*len(li)
    b = n - (l*len(s))
    for i in range(0,b):
        if(s[i] == "a"):
            c = c +1 
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
