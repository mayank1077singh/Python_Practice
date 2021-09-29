#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #x=s.split()
   # print(x[0].capitalize())
    #j=len(x)
   #print(x[1].capitalize())
    #for i in range(0,j):
     #   x[i]=x[i].capitalize()
        
     # Join the string based on '-' delimiter 
   # s2 = ' '.join(x) 
    for x in s[:].split(): s = s.replace(x, x.capitalize())


    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

