import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
C = Counter(A)

print(*[C[b] for b in B])
