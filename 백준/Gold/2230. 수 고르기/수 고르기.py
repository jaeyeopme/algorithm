import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

left, right = 0, 0
min_d = float('inf')

while left < N and right < N:
  d = A[right] - A[left]

  if d < M:
    right += 1
  else:
    min_d = min(min_d, d)
    left += 1
    
    if min_d == M:
      break

print(min_d)
