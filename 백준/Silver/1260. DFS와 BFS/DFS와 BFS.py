from collections import defaultdict
from collections import deque

N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    for g in graph:
        graph[g].sort(reverse=True)

    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


def bfs(start):
    for g in graph:
        graph[g].sort()

    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


dfs(V)
print()
bfs(V)
