import sys

input = sys.stdin.readline

N = int(input())
L = sorted(list(map(int, input().split())))
S = float("inf")
ans = []

l, r = 0, N - 1

while l < r:
    v = L[l] + L[r]
    t = abs(v)

    if t < S:
        S = t
        ans = [L[l], L[r]]

    if v < 0:
        l += 1
    else:
        r -= 1

print(*ans)
