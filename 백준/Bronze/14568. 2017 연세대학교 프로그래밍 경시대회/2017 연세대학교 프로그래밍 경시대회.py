N = int(input())
ans = 0

# 택희
for A in range(1, N):
    # 영훈
    for B in range(1, N):
        # 남규
        for C in range(1, N):
            if A + B + C == N and C >= B + 2 and A % 2 == 0:
                ans += 1

print(ans)