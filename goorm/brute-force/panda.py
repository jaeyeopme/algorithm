N, M, K = map(int, input().split())
pandas = [tuple(map(int, input().split())) for _ in range(K)]
ans = float("inf")

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if (r, c) in pandas:
            continue
        t = 0
        for R, C in pandas:
            t += (r - R) ** 2 + (c - C) ** 2
        ans = min(ans, t)

print(ans)
