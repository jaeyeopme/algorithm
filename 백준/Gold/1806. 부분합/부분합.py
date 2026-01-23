import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
current_sum, min_len = 0, float("inf")

while True:
  if current_sum >= S:
    min_len = min(min_len, end - start)
    current_sum -= A[start]
    start += 1
  elif end < N:
    current_sum += A[end]
    end += 1
  else:
    break

print(0 if min_len == float("inf") else min_len)