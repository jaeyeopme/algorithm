N, M = map(int, input().split())
# 아이템 이름이 모두 다름
A = set(input().split())
B = set(input().split())
exchange = [input().split() for _ in range(M)]

for Ai, Bi in exchange:
    # 각 A, B 가 Ai, Bi 를 가지고 있을 때에만 교환이 이뤄짐
    if Ai in A and Bi in B:
        A.remove(Ai)
        A.add(Bi)
        B.remove(Bi)
        B.add(Ai)

print(*sorted(A))
