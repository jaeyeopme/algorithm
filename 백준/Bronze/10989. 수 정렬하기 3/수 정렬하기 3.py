import sys

input = sys.stdin.readline

N = int(input())
map = dict()

for _ in range(N):
    x = int(input())

    if x in map:
        map[x] += 1
    else:
        map[x] = 1

for k in sorted(list(map.keys())):
    for i in range(map[k]):
        print(k)
