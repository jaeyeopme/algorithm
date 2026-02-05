import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
T = input().strip()

current_count = defaultdict(int)
start, end = 0, 0
ans = 0

for end in range(len(T)):
    current_count[T[end]] += 1

    while len(current_count) > N:
        current_count[T[start]] -= 1
        if current_count[T[start]] == 0:
            del current_count[T[start]]
        start += 1

    ans = max(ans, end - start + 1)

print(ans)
