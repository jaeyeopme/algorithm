import sys

input = sys.stdin.readline

N, K = map(int, input().split())
circle = list(range(1, N + 1))
current = 0
ans = []

while circle:
    actual = (current + (K - 1)) % len(circle)
    ans.append(str(circle.pop(actual)))
    current = actual

print(f"<{', '.join(ans)}>")
