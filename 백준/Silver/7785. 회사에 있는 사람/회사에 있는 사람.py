import sys

input = sys.stdin.readline

n, r = int(input()), set()

for _ in range(n):
    name, commute = input().split()
    
    if commute == "enter":
        r.add(name)
        continue

    if name in r:
        r.remove(name)

print(*sorted(r, reverse=True), sep="\n")