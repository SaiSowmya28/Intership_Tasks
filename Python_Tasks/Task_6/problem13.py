# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
c=s1.union(s2)
print(len(c))
