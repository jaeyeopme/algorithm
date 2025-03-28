def hanoi(n, start, end, via):
    if n == 1:
        moves.append((start, end))
        return
    hanoi(n - 1, start, via, end)
    moves.append((start, end))  # 움직임을 기록
    hanoi(n - 1, via, end, start)


K = int(input())
sticks = [[i for i in range(20, 0, -1)], [], []]
moves = []

hanoi(20, 0, 2, 1)

for i in range(K):
    start, end = moves[i]
    sticks[end].append(sticks[start].pop())

print(*[sum(stick) for stick in sticks])
