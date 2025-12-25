import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

last_end_time, count = 0, 0

for start, end in sorted(meetings, key=lambda x: (x[1], x[0])):
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
