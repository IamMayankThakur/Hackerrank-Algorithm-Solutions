#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = 0
    for i in apples:
        if((a + i) >= s and (i+a) <= t ):
            ap = ap+1
       # print (a+i)
    print(ap)
    o  = 0
    for j in oranges:
        if((j + b) >= s and j + b <= t ):
            o = o +1 
    print(o)




if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)