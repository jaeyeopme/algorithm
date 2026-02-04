import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
left, right = 0, 0

while left < N or right < M:
    if left < N and right == M:
        ans.append(A[left])
        left += 1
        continue
    if right < M and left == N:
        ans.append(B[right])
        right += 1
        continue

    if A[left] < B[right]:
        ans.append(A[left])
        left += 1
    else:
        ans.append(B[right])
        right += 1

print(*ans)
