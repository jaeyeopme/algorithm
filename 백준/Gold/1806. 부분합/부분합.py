import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

start = 0
current_sum, min_len = 0, N + 1

for end in range(N):
  current_sum += A[end]

  while current_sum >= S:
    min_len = min(min_len, end - start + 1)
    current_sum -= A[start]
    start += 1

print(0 if min_len == N + 1 else min_len)
