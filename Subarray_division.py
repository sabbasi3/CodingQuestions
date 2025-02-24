#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    count = 0 
    for left in range(len(s) - m +1):
        right = left + m 
        sumval = sum(s[left:right])
        if sumval == d:
            count += 1
    return count
        

### Other implementation where you subtract the previous value and add the next value    
# def birthday(s, d, m):
#     count = 0
#     current_sum = sum(s[:m])  # Initial sum of the first window
    
#     # Check the initial window
#     if current_sum == d:
#         count += 1
    
#     # Slide the window across the array
#     for i in range(len(s) - m):
#         current_sum = current_sum - s[i] + s[i + m]  # Slide the window
#         if current_sum == d:
#             count += 1
    
#     return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
