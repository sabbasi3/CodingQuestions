#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#
from collections import defaultdict

def matchingStrings(strings, queries):
    # Write your code here
    newdict = defaultdict(int)
    results = []
    for s in strings:
        newdict[s] += 1
    for q in queries: 
        results.append(newdict[q])
    
    return results
    
    # sdict = {}
    # results = []
    # for stringword in strings:
    #     sdict[stringword] = sdict.get(stringword, 0) + 1
    
    # for q in queries:
    #     results.append(sdict.get(q,0))

    # return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
