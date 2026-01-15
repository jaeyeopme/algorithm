import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
ans = 1

start, end = 1, max(lans)

while start <= end:
  mid = (start + end) // 2
  count = sum([lan // mid for lan in lans if lan >= mid])

  if count >= N:
    ans = mid
    start = mid + 1
  elif count < N:
    end = mid - 1

print(ans)
