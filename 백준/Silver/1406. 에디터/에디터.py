import sys

input = sys.stdin.readline

T = list(input().strip())
M = int(input())
left, right = T, []

for _ in range(M):
    command = input().strip()

    if command == "L":
        if left:
            right.append(left.pop())
        continue

    if command == "D":
        if right:
            left.append(right.pop())
        continue

    if command == "B":
        if left:
            left.pop()
        continue

    left.append(command.split()[1])

print(*left + right[::-1], sep="")
