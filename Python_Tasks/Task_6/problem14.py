# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
c=s1.intersection(s2)
print(len(c))
