import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

scores = {}
merged_scores = []
chips = {}

for _ in range(N):
    line = input().split()
    N, C = line[0], int(line[1])

    if C < X * 0.05:
        continue

    chips[N] = 0

    for i in range(14):
        value = C / (i + 1)
        scores[value] = N
        merged_scores.append(value)

last_scores = sorted(merged_scores, reverse=True)[:14]

for s in last_scores:
    name = scores[s]
    chips[name] += 1

for name in sorted(chips.keys()):
    print(name, chips[name])
