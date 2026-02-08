import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input().strip() for _ in range(N)])
ans = []

for _ in range(M):
    name = input().strip()
    if name in S:
        ans.append(name)

print(len(ans), *sorted(ans), sep="\n")
