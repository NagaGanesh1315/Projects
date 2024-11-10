#!/bin/python3
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    arr.sort() # sort you array first
    min_sum = sum(arr[:4]) # eliminate max number and calculate min_sum
    max_sum = sum(arr[1:]) # eliminate min number and calculate max_sum
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
