import sys

input = sys.stdin.readline

N, P = int(input()), list()

for i in range(N):
    age, name = input().split()
    P.append([int(age), name])

for age, name in sorted(P, key=lambda x: (x[0])):
    print(age, name)
