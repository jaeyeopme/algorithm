import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    Y, X = 0, 1
    for i in range(N):
        Y += 1
        if Y == H:
            if i == N - 1:
                break
            Y = 0
            X += 1

    print(f"{Y}{X:02d}")