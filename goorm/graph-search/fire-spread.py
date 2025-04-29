from collections import deque


def bfs():
    while queue:
        cx, cy = queue.popleft()

        for dx, dy in direc:
            x, y = cx + dx, cy + dy

            if -1 < x < R and -1 < y < C:
                if (x, y) not in visited:  # 불 옮기기
                    visited.add((x, y))
                    queue.append((x, y))
                    dist[x][y] = dist[cx][cy] + 1

    if goorm not in visited:  # 구름에게 도달하지 못한 것임
        print(-1)
    else:
        x, y = goorm
        print(dist[x][y] - 1)


R, C = map(int, input().split())
labs = [[None] * C for _ in range(R)]
dist = [[0] * C for _ in range(R)]  # 거리 저장

direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]

queue = deque()
goorm = ()
visited = set()

for r in range(R):
    row = list(input())
    for c in range(C):
        labs[r][c] = row[c]

        if labs[r][c] == "#":
            visited.add((r, c))  # 벽 방문 처리
            continue

        if labs[r][c] == "&":
            goorm = (r, c)  # 구름 위치 저장
            continue

        if labs[r][c] == "@":
            queue.append((r, c))  # !불이 여러 개 있을 수 있음
            visited.add((r, c))

bfs()
