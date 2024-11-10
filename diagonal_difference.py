#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    
    left_right_sum = 0
    right_left_sum = 0
    n = len(arr)
    
    for i in range(n):
        left_right_sum = left_right_sum + arr[i][i]
        right_left_sum = right_left_sum + arr[i][n - i - 1]
    
    difference = abs(left_right_sum - right_left_sum)
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
