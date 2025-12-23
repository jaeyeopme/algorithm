import sys

input = sys.stdin.readline

N = int(input())
p = list()

for i in range(N):
    age, name = input().split()
    p.append([int(age), name])

for age, name in sorted(p, key=lambda x: (x[0])):
    print(age, name)
