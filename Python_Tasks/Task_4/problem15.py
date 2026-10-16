# Word Order
# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for i in range(n):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len(d))
for value in d.values():
    print(value,end=' ')
