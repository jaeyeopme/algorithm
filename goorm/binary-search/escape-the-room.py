import bisect

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [int(input()) for _ in range(M)]

A.sort()

for b in B:
    idx = bisect.bisect_left(A, b)
    print(1 if idx < len(A) and A[idx] == b else 0)
