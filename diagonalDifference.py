#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    ldiag = 0
    rdiag = 0
    c1 = 0
    c2 = len(arr)-1
    for _ in range(len(arr)):
        ldiag += int(arr[c1][c1])
        rdiag += int(arr[c1][c2-c1])
        c1 +=1
    difference = abs(ldiag-rdiag)
    return difference
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
