N, K = map(int, input().split())
clouds = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
ans = 0

for r in range(N):
    for c in range(N):
        if clouds[r][c] == 1:
            continue

        count = 0

        for dr, dc in directions:
            tr = r + dr
            tc = c + dc

            if 0 <= tr < N and 0 <= tc < N:
                if clouds[tr][tc] == 1:
                    count += 1

        if count == K:
            ans += 1

print(ans)
