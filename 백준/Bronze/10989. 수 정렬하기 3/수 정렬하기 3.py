import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
map = defaultdict(int)

for _ in range(N):
    map[int(input())] += 1

for k in sorted(list(map.keys())):
    for i in range(map[k]):
        print(k)
