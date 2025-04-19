N, M = map(int, input().split())
cur_rate = int((M / N) * 100)
goal_rate = cur_rate + 1
ans = -1

start = 1
end = 10**12 - 1

while start <= end:
    mid = (start + end) // 2
    rate = int(((M + mid) / (N + mid)) * 100)

    # 최소 값 구하기
    if rate >= goal_rate:
        ans = mid
        end = mid - 1
        continue

    start = mid + 1

print("X" if ans == -1 else ans)
