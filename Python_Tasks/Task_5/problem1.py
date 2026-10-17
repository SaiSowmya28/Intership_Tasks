# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first=second=float('-inf')
    for i in arr:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    print(second)
        
