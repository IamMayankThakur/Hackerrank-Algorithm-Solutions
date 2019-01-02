#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if(s[len(s)-2] == "P"):
        if(s[0] == "1" and s[1] == "2"):
            return s[:8]
        k = s.split(":")
        k[0] = str(int(k[0]) + 12)
        m = ":"
        return m.join(k)[:8]
    if(s[len(s)-2] == "A" and s[0] == "1" and s[1] == "2"):
        k = s.split(":")
        k[0] = "00"
        m = ":"
        return m.join(k)[:8]
    return s[:8]



    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()