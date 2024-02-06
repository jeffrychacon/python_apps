#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    
    for element in arr:
        if (element>0) and (element<100):
            positive +=1
        elif (element < 0) and (element> -100):
            negative +=1
        elif (element == 0):
            zero+=1
    
    size =  len(arr)
    positive_ratio =  round(positive/size,6)
    negative_ratio = round(negative/size,6)
    zero_ratio = round(zero/size,6)
    
    print(f"{positive_ratio}")
    print(f"{negative_ratio}")
    print(f"{zero_ratio}")
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
