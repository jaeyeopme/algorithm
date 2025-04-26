T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    [input() for _ in range(M)]
    print(N - 1)  # minimum spanning tree
