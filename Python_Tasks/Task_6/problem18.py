# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
op=int(input())
for i in range(op):
    command,value=input().split()
    value=int(value)
    b=set(map(int,input().split()))
    if command=='intersection_update':
        a.intersection_update(b)
    elif command=='update':
        a.update(b)
    elif command=='symmetric_difference_update':
        a.symmetric_difference_update(b)
    elif command=='difference_update':
        a.difference_update(b)
print(sum(a))
