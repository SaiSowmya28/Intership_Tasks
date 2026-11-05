# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
rooms=list(map(int,input().split()))
unique_rooms=set(rooms)
captin=(sum(unique_rooms)*k-sum(rooms))//(k-1)
print(captin)
