A, B, C = map(int, input().split())
N = int(input())
products = [tuple(map(int, input().split())) for _ in range(N)]
count, price = 0, 0

products.sort(key=lambda x: x[0])

for p, t in products:
    # A: X 충전기, B: Y 충전기, C: 둘 다
    if t == 0:  # X
        if A > 0:
            A -= 1
            count += 1
            price += p
        elif C > 0:
            C -= 1
            count += 1
            price += p
    if t == 1:  # Y
        if B > 0:
            B -= 1
            count += 1
            price += p
        elif C > 0:
            C -= 1
            count += 1
            price += p

print(count, price)
