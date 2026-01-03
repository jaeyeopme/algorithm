import sys

input = sys.stdin.readline

N, M, T = map(int, input().split())
K, a, b = map(int, input().split())
graph = []

for i in range(1, N + 1):
    graph.append(list(input().strip()))

for _ in range(T):
    pre_graph = [[0] for _ in range(N + 1)]
    pre_graph[0] = [0] * (M + 1)

    # x prefix
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            me = 1 if graph[i - 1][j - 1] == '*' else 0
            pre_graph[i].append(pre_graph[i][-1] + me)

    # y prefix
    for j in range(1, M + 1):
        for i in range(1, N + 1):
            pre_graph[i][j] += pre_graph[i - 1][j]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            sx, sy, ex, ey = max(i - K, 1), max(j - K, 1), min(i + K, N), min(j + K, M)

            left = pre_graph[ex][sy - 1]
            top = pre_graph[sx - 1][ey]
            overlap = pre_graph[sx - 1][sy - 1]
            me = 1 if graph[i - 1][j - 1] == '*' else 0

            around = (pre_graph[ex][ey] - (left + top)) + overlap - me

            if graph[i - 1][j - 1] == '*':
                if a <= around <= b:
                    continue
                graph[i - 1][j - 1] = '.'
            else:
                if a < around <= b:
                    graph[i - 1][j - 1] = '*'

for i in range(N):
    print("".join(graph[i]))
