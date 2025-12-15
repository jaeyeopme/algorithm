import sys

input = sys.stdin.readline
all_permu = [int((n * (n + 1)) / 2) for n in range(1, 45)]
len_permu = len(all_permu)
permu = []

for a in range(len_permu):
    for b in range(len_permu):
        if all_permu[a] + all_permu[b] > 1000:
            continue
            
        for c in range(len_permu):
            sum = all_permu[a] + all_permu[b] + all_permu[c]
            if sum > 1000:
                continue

            if sum <= 1000: permu.append(sum)


print(*[int(x in permu) for x in [int(input()) for _ in range(int(input()))]], sep="\n")
