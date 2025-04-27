from collections import defaultdict


def dfs(current_island):
    stack = [current_island]

    while stack:
        island = stack.pop()

        if island in union:
            continue

        union.add(island)

        for neighbor in union_graph[island]:
            if neighbor not in union:
                stack.append(neighbor)


N, M = map(int, input().split())
island_infos = set()
union_graph = defaultdict(list)
union = set()
ans = 0

for _ in range(M):
    si, ei = map(int, input().split())
    island_infos.add((si, ei))

for si, ei in island_infos:
    # 양방향 다리가 있는 연합이라면 연합 그래프에 추가
    if (ei, si) in island_infos:
        union_graph[ei].append(si)
        union_graph[si].append(ei)

# 1부터 N까지 섬들을 순회
for island in range(1, N + 1):
    # 연합 등록을 하지 않은 섬의 인접 섬 탐색
    if island not in union:
        ans += 1
        # 연합 탐색
        dfs(island)

print(ans)
