# 연속된 수 중 가장 큰 합을 구해야 함
N = int(input())
arr = list(map(int, input().split()))
prefix = [-1001] * (N + 1)

# 누적할 값이 누적된 값보다 크다면 누적된 값을 버림
for i in range(N):
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))
