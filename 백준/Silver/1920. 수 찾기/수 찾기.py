import sys

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
T = list(map(int, input().split()))

for t in T:
    found = False
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2
        if t < A[mid]:
            r = mid - 1
        elif t > A[mid]:
            l = mid + 1
        else:
            found = True
            break

    print(1 if found else 0)
