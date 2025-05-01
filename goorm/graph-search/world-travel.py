from collections import defaultdict, deque


def bfs(known_langs):
    # 1번 섬부터 시작
    queue = deque([1])
    visited = set([1])
    count = 1

    while queue:
        island = queue.popleft()

        for nei in graph[island]:
            lang = langs[nei - 1]

            # 이웃 섬 중 방문하지 않았고, 아는 언어라면 방문
            if nei not in visited and lang in known_langs:
                count += 1
                queue.append(nei)
                visited.add(nei)

    return count


N, M = map(int, input().split())
langs = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(M):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

# 최다 방문 횟수
max_count = 1

# 최대 언어 개수로 고정하고 시작
for lang in range(1, 11):
    if langs[0] == lang:
        continue
    max_count = max(max_count, bfs(set([langs[0], lang])))

print(max_count)
