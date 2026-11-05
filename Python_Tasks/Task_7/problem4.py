# Funny String
# https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys
def funnyString(s):
    n=len(s)
    for i in range(1,n):
        a=abs(ord(s[i])-ord(s[i-1]))
        b=abs(ord(s[n-i])-ord(s[n-i-1]))
        if a!=b:
            return 'Not Funny'
    return 'Funny'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()
