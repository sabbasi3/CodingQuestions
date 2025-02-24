#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    flipped = ~n
    result = flipped & 0xFFFFFFFF
    # In Python, applying the bitwise NOT operator to an integer results in a negative number because Python uses signed integers by default.
    #For example, ~5 results in -6 because ~n is equivalent to -(n + 1).
    # When you perform a bitwise AND (&) with 0xFFFFFFFF, it ensures that only the lower 32 bits of the result are considered, effectively masking out any higher bits that might be set due to the sign extension in Python's signed integers.
    
    return result
    
    # XOR with a mask of 32 bits all set to 1 (0xFFFFFFFF)
    # return n ^ 0xFFFFFFFF
    # 0 XOR 0 = 0
    # 0 XOR 1 = 1
    # 1 XOR 0 = 1
    # 1 XOR 1 = 0
    # return n ^ 0b11111111111111111111111111111111
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
