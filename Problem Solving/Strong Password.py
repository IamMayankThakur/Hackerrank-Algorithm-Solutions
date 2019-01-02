#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    l = [1,1,1,1]
    for i in password:
        if(i in "abcdefghijklmnopqrstuvwxyz"):
            l[0] = 0
        if(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            l[1] = 0
        if(i in "!@#$%^&*()-+"):
            l[2] = 0
        if(i in "0123456789"):
            l[3] = 0
             
    if(len(password)<6):
        if(l.count(1)>0 and l.count(1)>6-len(password)):
            return (6-len(password))+l.count(1)-(6-len(password))
        return 6-len(password)
    else:
        return l.count(1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
