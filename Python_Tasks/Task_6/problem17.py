# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())
result=True
for i in range(n):
    b=set(map(int,input().split()))
    if not(a.issuperset(b) and a!=b):
        result=False
        break
print(result)
