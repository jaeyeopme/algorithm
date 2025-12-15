import sys
from itertools import combinations

input = sys.stdin.readline

arr = combinations([int(input()) for _ in range(9)], 7)

for a in arr:
    if sum(a) == 100:
        [print(x) for x in sorted(a)]
        break
