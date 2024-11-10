#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    unique = []   
    repeated = []

    for i in a:
        if i in unique:
            unique.remove(i)
            repeated.append(i)
        elif i not in repeated:
            unique.append(i)
    return unique[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
