import sys
from itertools import combinations

input = sys.stdin.readline

arr = combinations([int(input()) for _ in range(9)], 7)

for x in arr:
    if sum(x) == 100:
        print(*sorted(x), sep="\n")
        break
