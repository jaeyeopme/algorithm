N = int(input())
coins = list(map(int, input().split()))

dp = [0] * N
dp[0] = coins[0]

# dp 에 누적 값 저장하기
for i in range(1, N):
    # 새로 줍는게 나은 경우 C[i] 부터 다시 누적
    dp[i] = max(dp[i - 1], 0) + coins[i]

dp.append(0)  # 동전을 아예 줍지 않을 수 있음
print(max(dp))
