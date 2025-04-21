N = int(input())
stock = {}

for _ in range(N):
    S, A = input().split()
    stock[S] = stock.get(S, 0) + int(A)

for key, value in sorted(stock.items()):
    print(key, value)
