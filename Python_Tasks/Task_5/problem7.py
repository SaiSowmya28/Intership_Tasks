# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
m_values=set(map(int,input().split()))
n=int(input())
n_values=set(map(int,input().split()))
s=set()
s.update(m_values.difference(n_values))
s.update(n_values.difference(m_values))
for i in sorted(s):
    print(i)
