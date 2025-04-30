from collections import defaultdict, deque


def bfs(start):
    queue = deque([start])
    visited = set()

    last = start
    count = 0

    while queue:
        node = queue.popleft()

        last = node
        count += 1
        visited.add(node)

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                # 방문 가능한 가장 작은 인접 노드
                queue.append(neighbor)
                break  # 바로 이동

    return count, last


N, M, K = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*bfs(K))
