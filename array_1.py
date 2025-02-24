import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    # Write your code here
    lefttotal = 0
    righttotal = 0
    r = n-1
    for i in range(n):
        lefttotal += arr[i][i]
        righttotal += arr[r][i]
        r = r -1
    total = abs(lefttotal - righttotal)
    
    return total 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
