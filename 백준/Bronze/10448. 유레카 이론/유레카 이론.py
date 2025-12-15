import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(int(input()))]
all_permu = [int((n * (n + 1)) / 2) for n in range(1, 45)]
len_permu = len(all_permu)
permu = []

for a in range(len_permu):
    for b in range(len_permu):
        for c in range(len_permu):
            permu.append(all_permu[a] + all_permu[b] + all_permu[c])

print(*[int(x in permu) for x in arr], sep="\n")
