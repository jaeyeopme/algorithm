import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N + 1)]
prefix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    graph[i + 1] = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = prefix[i][j - 1] + graph[i][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] += prefix[i - 1][j]

for _ in range(M):
    fx, fy, tx, ty = list(map(int, input().split()))

    whole = prefix[tx][ty]
    top_part = prefix[fx - 1][ty]
    left_part = prefix[tx][fy - 1]
    overlap = prefix[fx - 1][fy - 1]

    print(whole - (top_part + left_part) + overlap)
