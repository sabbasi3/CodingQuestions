# def pangrams(s):
#     # Create a set of all alphabetic characters in the input string, converted to lowercase
#     unique_letters = set(char.lower() for char in s if char.isalpha())
    
#     # Check if the set contains all 26 letters of the alphabet
#     if len(unique_letters) == 26:
#         return "pangram"
#     else:
#         return "not pangram"


def pangrams(s):
    # Write your code here
    uniqueletters = set()
    
    for char in s:
        if char.isalpha():
            uniqueletters.add(char.lower())
    
    if len(uniqueletters) == 26:
        return "pangram"
    else:
        return "not pangram"
    
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    letters = {}
    allletters = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char.isalpha():
            if char in letters:
                letters[char.lower()] += 1
            else:
                letters[char.lower()] = 1

    for s in allletters:
        
        if s not in letters:
            return "not pangram"
              
            
    return "pangram"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
