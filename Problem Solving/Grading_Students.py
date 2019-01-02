#!/bin/python

from __future__ import print_function

import os
import sys
import math
#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    k = list()
    for i in grades:
        if(i>37):
            if(5*(math.floor(i/5)+1) - i < 3):
                i = 5*(math.floor(i/5)+1)
        k.append(int(i))
    return k
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')
    f.close()
