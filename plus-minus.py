#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Initialize counters
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    # Increment positive, negative, and zero counts
    for n in arr:
        if n > 0:
            pos = pos + 1
        elif n < 0:
            neg = neg + 1
        else:
            zero = zero + 1
            
    # Calculate the ratios
    print(f"{pos/total:.6f}")
    print(f"{neg/total:.6f}")
    print(f"{zero/total:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
