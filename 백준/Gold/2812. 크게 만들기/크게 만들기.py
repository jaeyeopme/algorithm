import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
T = [int(t) for t in input().strip()]
S = []

for t in T:
    while S and S[-1] < t and K > 0:
        S.pop()
        K -= 1
    S.append(t)

print(*S[:-K] if K > 0 else S, sep='')
