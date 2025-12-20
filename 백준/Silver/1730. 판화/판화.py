import sys

input = sys.stdin.readline


def mark(y, x, cmd):
    global grid

    if grid[y][x] == "+": return
    current = grid[y][x]

    if cmd in vertical:
        if current == "-":
            grid[y][x] = "+"
            return
        grid[y][x] = "|"
        return

    if current == "|":
        grid[y][x] = "+"
        return
    grid[y][x] = "-"


N = int(input())
commands = input().strip()
grid = [["."] * N for _ in range(N)]

dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
vertical = {"U", "D"}

y, x = 0, 0

for cmd in commands:
    ny, nx = y + dy[cmd], x + dx[cmd]

    if -1 < ny < N and -1 < nx < N:
        # current
        mark(y, x, cmd)
        # next
        mark(ny, nx, cmd)
        # swap
        y, x = ny, nx

[print("".join(row)) for row in grid]
