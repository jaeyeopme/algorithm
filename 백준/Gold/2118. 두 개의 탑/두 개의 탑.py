import sys

input = sys.stdin.readline

N = int(input())
D = [int(input()) for _ in range(N)]
T = sum(D)
ans = 0

start, end = 0, 1
current = sum(D[start:end])

while end < N:
  right = current
  left = T - right

  if right < left:
    current += D[end]
    end += 1
  else:
    current -= D[start]
    start += 1

  ans = max(ans, min(right, left))

print(ans)