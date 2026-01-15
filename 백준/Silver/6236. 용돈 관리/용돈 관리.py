import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
ans = 0
start, end = max(A), sum(A)

while start <= end:
  K = (start + end) // 2
  remain, count = K, 1

  for a in A:
    if remain < a:
      remain = K
      count += 1
    remain -= a

  if count > M:
    start = K + 1
  else:
    ans = K
    end = K - 1

print(ans)
