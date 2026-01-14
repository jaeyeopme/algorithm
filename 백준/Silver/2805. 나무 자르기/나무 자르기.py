import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
ans = start

while start <= end:
  mid = (start + end) // 2
  total = sum(tree - mid for tree in trees if tree > mid)

  if total >= M:
    ans = mid
    start = mid + 1
  elif total < M:
    end = mid - 1

print(ans)
