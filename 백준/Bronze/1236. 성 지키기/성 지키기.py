N, M = map(int, input().split(" "))
arr = [list(input()) for _ in range(N)]

row, column = [False] * M, [False] * N
rCount, cCount = M, N

for i in range(N):
    for j in range(M):
        if arr[i][j] == "X":
            if not row[j]:
                row[j] = True
                rCount -= 1
            if not column[i]:
                column[i] = True
                cCount -= 1

print(max(rCount, cCount))
