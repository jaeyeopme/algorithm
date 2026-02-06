import sys

input = sys.stdin.readline

N, K = map(int, input().split())
circle = list(range(1, N + 1))
ans = []
next = 0

while circle:
    step = next + (K - 1)
    next = step % len(circle)
    ans.append(circle.pop(next))

print("<" + ", ".join(map(str, ans)) + ">")
