def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# connect graph
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
count = 0

for item in range(1, N + 1):
    if not visited[item]:
        dfs(item)
        count += 1

print(count)
