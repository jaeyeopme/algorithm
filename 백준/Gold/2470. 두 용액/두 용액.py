import sys

input = sys.stdin.readline

N = int(input())
L = sorted(list(map(int, input().split())), key=lambda x: abs(x))
S = float('inf')
ans = ()

for i in range(N - 1):
    s = L[i] + L[i + 1]

    if abs(s) < S:
        S = abs(s)
        ans = [L[i], L[i + 1]]

print(*sorted(ans))
