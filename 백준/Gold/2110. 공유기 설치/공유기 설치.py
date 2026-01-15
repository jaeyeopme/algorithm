import sys

input = sys.stdin.readline

N, C = map(int, input().split())
L = sorted([int(input()) for _ in range(N)])
ans = 0
start, end = 1, L[-1] - L[0]

while start <= end:
  mid = (start + end) // 2
  last, count = L[0], 1

  for i in range(1, N):
    if L[i] - last >= mid:
      count += 1
      last = L[i]

  if count >= C:
    ans = mid
    start = mid + 1
  else:
    end = mid - 1

print(end)
