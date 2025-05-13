MOD, REST = 10**9 + 7, -1
N, M, K = map(int, input().split())
rests = set([tuple(map(int, input().split())) for _ in range(K)])
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 출발지 초기화
dp[1][1] = 1

for r in range(1, N + 1):
    for c in range(1, M + 1):
        for k in range(1, 7):
            # 위에서 오는 경로 수 누적
            if r - k >= 1 and (r - k, c) not in rests:
                dp[r][c] += dp[r - k][c]
                dp[r][c] %= MOD
            # 왼쪽에서 오는 경로 수 누적
            if c - k >= 1 and (r, c - k) not in rests:
                dp[r][c] += dp[r][c - k]
                dp[r][c] %= MOD

print(dp[N][M])
