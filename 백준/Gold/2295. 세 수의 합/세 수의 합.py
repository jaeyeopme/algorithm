import sys

input = sys.stdin.readline

N = int(input())
U = sorted([int(input()) for _ in range(N)], reverse=True)
XY = set([U[i] + U[j] for i in range(N) for j in range(i, N)])

for k in U:
    found = False

    for z in U:
        if k - z in XY:
            print(k)
            found = True
            break

    if found: break
