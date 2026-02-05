import sys

input = sys.stdin.readline

N, B, W = map(int, input().split())
P = input().strip()
ans = 0

cp = []
cb, cw = 0, 0
start, end = 0, 0

while end < N:
    if P[end] == "W":
        cw += 1
    else:
        cb += 1

    while cb > B:
        if P[start] == "W":
            cw -= 1
        else:
            cb -= 1
        start += 1

    if cw >= W:
        ans = max(ans, end - start + 1)

    end += 1

print(ans)
