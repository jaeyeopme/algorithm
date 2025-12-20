import sys

input = sys.stdin.readline


def mark(y, x):
    global lattice

    if lattice[y][x] == ".":
        if c == "U" or c == "D":
            lattice[y][x] = "|"
        else:
            lattice[y][x] = "-"

    if lattice[y][x] == "-" and (c == "U" or c == "D"):
        lattice[y][x] = "+"

    if lattice[y][x] == "|" and (c == "L" or c == "R"):
        lattice[y][x] = "+"


N = int(input())
commands = list(input())
direc = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
lattice = [["."] * N for _ in range(N)]

current = (0, 0)
for c in commands:
    if c not in direc:
        continue
    cy, cx = current
    dy, dx = direc[c]
    ny, nx = cy + dy, cx + dx

    if -1 < cx < N and -1 < cy < N and -1 < nx < N and -1 < ny < N:
        # current
        mark(cy, cx)
        # next
        mark(ny, nx)
        # swap
        current = ny, nx

[print(*x, sep="") for x in lattice]
