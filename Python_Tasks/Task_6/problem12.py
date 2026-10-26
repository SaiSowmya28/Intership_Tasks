# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(N):
    command=input().split()                # code is correct but in the input the first operation is pop ,set is unorderd then 9 is removed in first
    if command[0]=='remove':               # then next operation is remove 9 so i am getting error there
        s.remove(int(command[1]))
    elif command[0]=='discard':
        s.discard(int(command[1]))
    elif command[0]=='pop':
        s.pop()
print(sum(s))
