# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
X = int(input())
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)
N = int(input())
total = 0
for _ in range(N):
    size, price = map(int, input().split())

    if inventory[size] > 0:
        total += price
        inventory[size] -= 1
print(total)
