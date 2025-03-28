N = int(input())

for i in range(N):
    j = i + 1
    print(' ' * (N - j) + '*' * j)
    