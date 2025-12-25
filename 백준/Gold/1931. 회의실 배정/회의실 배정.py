import sys

input = sys.stdin.readline

N = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

last_end_time, count = 0, 0

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
