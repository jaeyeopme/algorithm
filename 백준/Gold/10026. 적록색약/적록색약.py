def dfs(i, j, is_rg=False):
    stack = [(i, j)]
    visited[i][j] = True

    while stack:
        (px, py) = stack.pop()

        for ix, iy in search_points:
            x, y = px + ix, py + iy

            if not (0 <= x < N and 0 <= y < N):
                continue

            if not visited[x][y] and grid[px][py] == grid[x][y]:
                visited[x][y] = True
                stack.append((x, y))
                continue

            if (
                is_rg
                and not visited[x][y]
                and (grid[px][py] in ["R", "G"])
                and (grid[x][y] in ["R", "G"])
            ):
                visited[x][y] = True
                stack.append((x, y))


N = int(input())
grid = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
search_points = [(0, -1), (1, 0), (0, 1), (-1, 0)]
count = 0
rg_count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            dfs(i, j)

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            rg_count += 1
            dfs(i, j, True)

print(count, rg_count)
