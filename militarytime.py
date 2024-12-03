#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s1=s.split(':')
    sm = ''
    minute = s1[1]
    second = s1[2]
    if "PM" in s:
        hour =  s1[0]
        s2= second.replace('PM','')
        if hour != '12':
            hour = int(hour) + 12 
    else: 
        hour =  s1[0]
        s2= second.replace('AM','')
        if hour == '12':
            hour = '00'
    sm = str(hour)+':'+minute+':'+s2
    return sm
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
