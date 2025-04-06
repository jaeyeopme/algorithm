def dfs(num):
    if num > K:
        global ans
        ans = min(ans, num)
        return

    for i in range(N):
        next_num = num * 10 + A[i]
        if next_num:
            dfs(next_num)


N = int(input())
A = list(map(int, input().split()))
K = int(input())
ans = float("inf")

dfs(0)
print(ans)
