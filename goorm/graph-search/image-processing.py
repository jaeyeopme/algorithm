def dfs(current_point):
    stack = [current_point]
    size = 0

    while stack:
        point = stack.pop()

        if point in visited:
            continue

        visited.add(point)
        size += 1

        # 인접 픽셀 확인
        for dx, dy in points:
            x, y = point[0] + dx, point[1] + dy
            # 그리드 범위 확인
            if -1 < x < M and -1 < y < N:
                if (x, y) not in visited and grid[x][y] == "#":
                    stack.append((x, y))

    return size


N, M = map(int, input().split())
grid = [list(input()) for _ in range(M)]
points = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = set()
count = 0
largest = float("-inf")

for i in range(M):
    for j in range(N):
        # 순회하면서 탐색
        print(i, j)
        if (i, j) not in visited and grid[i][j] == "#":
            count += 1
            largest = max(largest, dfs((i, j)))

print(count, largest, sep="\n")
