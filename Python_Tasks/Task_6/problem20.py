# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    s=input()
    if len(s)==10 and (s[0]=='9' or s[0]=='8' or s[0]=='7') and s.isdigit():
        print("YES")
    else:
        print("NO")
