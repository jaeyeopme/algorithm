from collections import deque


# 모든 간선의 가중치가 동일한(Z) 그래프에서의 최단 거리는 BFS로 해결할 수 있음
def bfs(start, end):
    (sx, sy), (ex, ey) = start, end
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0

    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in direcs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                # 이동 가능하고, 가지 않았던 길
                if grid[nx][ny] != 1 and dist[nx][ny] == -1:
                    # 증가된 거리를 dist에 기록
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist[ex][ey]


N, M = map(int, input().split())
X, Y, Z = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
coords = [list(map(int, input().split())) for _ in range(M)]

# 좌표가 거꾸로 들어옴
moves = [[(b - 1, a - 1), (d - 1, c - 1)] for a, b, c, d in coords]  # 0 based
direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 시작 위치
pre = moves[0][0]
total = 0

for i in range(M):
    start, end = moves[i]

    # 승차 지점으로 이동
    pre_move = bfs(pre, start)
    # 하차 지점으로 이동
    move = bfs(start, end)

    # 다음 승차 지점 등록
    pre = end

    if move > 5:
        # 기본 요금에 추가로 초과한 거리 1당 Y의 추가 요금
        total += X + (move - 5) * Y
    else:
        total += X

    total -= (pre_move + move) * Z

print(total)
