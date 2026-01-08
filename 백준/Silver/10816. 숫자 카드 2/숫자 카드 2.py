import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
MA = {}
ans = []

for a in A:
    if a in MA:
        MA[a] += 1
    else:
        MA[a] = 1

for b in B:
    if b in MA:
        ans.append(MA[b])
    else:
        ans.append(0)

print(*ans)
