#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if(x1 == x2):
        return("YES")
    if((x1<x2 and v1<=v2) or (x2<x1 and v2<=v1)):
        return("NO")
    elif(x1<x2 and v1>v2):
        k1 = x1
        k2 = x2
        while(1):  
            k1 = k1 + v1
            k2 = k2 + v2
            if(k1 == k2):
                return("YES")
                f = 0
            if(k1>k2):
                return("NO")
    else:
        k1 = x1
        k2 = x2
        while(1):  
            k1 = k1 + v1
            k2 = k2 + v2
            if(k1 == k2):
                return("YES")
                f = 0
            if(k1<k2):
                return("NO")
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
