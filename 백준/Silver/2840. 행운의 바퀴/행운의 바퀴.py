import sys

input = sys.stdin.readline

N, K = map(int, input().split())
spinner = ["?"] * N
prev = 0

for S, L in [input().split() for _ in range(K)]:
    cur = (prev - int(S)) % N

    if spinner[cur] != "?" and spinner[cur] != L:
        spinner = ["!"]
        break

    if spinner[cur] == L:
        spinner[cur] = "?"

    if L in spinner:
        spinner = ["!"]
        break

    spinner[cur] = L
    prev = cur

print(*(spinner[prev:] + spinner[:prev]), sep="")
