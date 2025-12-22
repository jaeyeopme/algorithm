import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

scores = {}
merged_scores = []
chips = {}

for _ in range(N):
    N, C = input().split()
    C = int(C)

    if C < X * 0.05: continue

    chips[N] = 0

    for i in range(14):
        value = C / (i + 1)
        scores[value] = N
        merged_scores.append(value)

sorted_scores = sorted(merged_scores, reverse=True)[:14]

for score in sorted_scores:
    name = scores[score]
    chips[name] += 1

for name in sorted(chips.keys()):
    print(name, chips[name])
