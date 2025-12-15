import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(int(input()))]

permu = []

for a in range(1, 45):
    for b in range(1, 45):
        for c in range(1, 45):
            permu.append(sum([int((n * (n + 1)) / 2) for n in [a, b, c]]))

for x in arr:
    print(int(x in permu))
