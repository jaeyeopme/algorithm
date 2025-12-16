import sys

input = sys.stdin.readline


def check_row(i):
    global maxCount

    if -1 < i < N:
        maxRow, cumRow = 1, 1
        for k in range(N - 1):
            if bomboni[i][k] == bomboni[i][k + 1]:
                cumRow += 1
                maxRow = max(maxRow, cumRow)
                continue
            cumRow = 1
        maxCount = max(maxCount, maxRow)


def check_col(j):
    global maxCount

    if -1 < j < N:
        maxCol, cumCol = 1, 1
        for k in range(N - 1):
            if bomboni[k][j] == bomboni[k + 1][j]:
                cumCol += 1
                maxCol = max(maxCol, cumCol)
                continue
            cumCol = 1
        maxCount = max(maxCount, maxCol)


def exchange(a, b):
    temp = bomboni[a[0]][a[1]]
    bomboni[a[0]][a[1]] = bomboni[b[0]][b[1]]
    bomboni[b[0]][b[1]] = temp


N = int(input())
bomboni = [list(input()) for _ in range(N)]
maxCount = 1

for i in range(N):
    for j in range(N):
        check_row(i)
        check_col(j)

        # left
        if -1 < j - 1 and bomboni[i][j] != bomboni[i][j - 1]:
            exchange((i, j), (i, j - 1))
            check_col(j - 1)
            check_col(j)
            check_row(i)
            exchange((i, j), (i, j - 1))

        # right
        if j + 1 < N and bomboni[i][j] != bomboni[i][j + 1]:
            exchange((i, j), (i, j + 1))
            check_col(j)
            check_col(j + 1)
            check_row(i)
            exchange((i, j), (i, j + 1))

        # top
        if -1 < i - 1 and bomboni[i][j] != bomboni[i - 1][j]:
            exchange((i, j), (i - 1, j))
            check_row(i - 1)
            check_row(i)
            check_col(j)
            exchange((i, j), (i - 1, j))

        # bottom
        if i + 1 < N and bomboni[i][j] != bomboni[i + 1][j]:
            exchange((i, j), (i + 1, j))
            check_row(i)
            check_row(i + 1)
            check_col(j)
            exchange((i, j), (i + 1, j))

print(maxCount)
