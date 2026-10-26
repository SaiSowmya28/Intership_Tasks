# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
for i in range(N):
    m=int(input())
    a=set(map(int,input().split()))
    n=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))
