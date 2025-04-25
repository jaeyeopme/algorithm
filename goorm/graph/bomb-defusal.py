N, M = map(int, input().split())
edge = []
degree = [0] * (N + 1)
ans = []

for i in range(M):
    a, b = map(int, input().split())
    # 번호와 노드 쌍의 연결 정보를 저장
    edge.append((i, (a, b)))
    # 간선 개수 추가
    degree[a] += 1
    degree[b] += 1

for i, (a, b) in edge:
    # i번 노드 쌍의 간선 개수가 2개 이상이라면 잘라도 됨
    if degree[a] > 1 and degree[b] > 1:
        ans.append(i + 1)  # 1 based

if not ans:
    print(-1)
else:
    print(*ans)
