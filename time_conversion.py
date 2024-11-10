#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    minute_and_second = (s[2:8])
    hour = int(s[:2])
    
    if s[-2:] == "AM":
        if hour == 12:
            hour = 00
    else:
        if hour != 12:
            hour = hour + 12
    return f"{hour:02}{minute_and_second}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
