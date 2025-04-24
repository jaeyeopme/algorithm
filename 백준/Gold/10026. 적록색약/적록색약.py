def is_same(c1, c2, is_rg):
    if not is_rg:
        return c1 == c2
    return c1 in ["R", "G"] and c2 in ["R", "G"] or ("B" == c1 == c2)


def dfs(i, j, is_rg=False):
    stack = [(i, j)]
    visited[i][j] = True

    while stack:
        px, py = stack.pop()
        current_color = grid[px][py]

        for dx, dy in directions:
            nx, ny = px + dx, py + dy

            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue

            neighbor_color = grid[nx][ny]

            if is_same(current_color, neighbor_color, is_rg):
                visited[nx][ny] = True
                stack.append((nx, ny))


N = int(input())
grid = [list(input()) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0
rg_count = 0

visited = [[False] * N for _ in range(N)]
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
