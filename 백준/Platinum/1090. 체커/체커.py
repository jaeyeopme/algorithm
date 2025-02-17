N = int(input())
checks = [list(map(int, input().split())) for _ in range(N)]
x_coords = [x for x, _ in checks]
y_coords = [y for _, y in checks]
ans = [-1] * N

for x in x_coords:
    for y in y_coords:
        dist = []
        for x1, y1 in checks:
            dist.append(abs(x - x1) + abs(y - y1))
        dist.sort()
        acc = 0
        for k in range(N):
            acc += dist[k]
            if ans[k] == -1:
                ans[k] = acc
                continue
            ans[k] = min(acc, ans[k])

print(*ans)
