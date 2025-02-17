N = int(input())
checks = [tuple(map(int, input().split())) for _ in range(N)]
candidates = [(x, y) for x, _ in checks for _, y in checks]
ans = [float('inf')] * N

for cx, cy in candidates:
    dis = sorted(abs(cx - x) + abs(cy - y) for x, y in checks)
    acc = 0

    for i in range(N):
        acc += dis[i]
        ans[i] = min(ans[i], acc)

print(*ans)
