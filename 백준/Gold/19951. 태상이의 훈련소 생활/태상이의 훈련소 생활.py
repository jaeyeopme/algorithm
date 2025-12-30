import sys

input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
C = [list(map(int, input().split())) for _ in range(M)]
mark = [0] * (N + 1)
prefix = [0]
ans = []

for a, b, k in C:
    mark[a - 1] += k
    mark[b] -= k

for i in range(N):
    prefix.append(mark[i] + prefix[-1])

for i in range(N):
    print(H[i] + prefix[i + 1], end=' ')
