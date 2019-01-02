#!/bin/python

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    m = 0
    for i in word:
        m = max(m,h[abs(ord("a")-ord(i))])
    return m*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = map(int, raw_input().rstrip().split())

    word = raw_input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
