N = int(input())
A = list(map(int, input().split()))
K = int(input())
ans = 0


def bfs(num):
    global ans
    sum = num + ans

    if sum > ans:
        ans = min(ans, sum)

    for i in range(N):
        bfs(A[i])

print(bfs(0))