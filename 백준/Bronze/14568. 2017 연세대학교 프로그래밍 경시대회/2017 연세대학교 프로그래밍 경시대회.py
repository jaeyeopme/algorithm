N = int(input())
result = 0

for A in range(1, N):
    for B in range(1, N):
        for C in range(1, N):
            if A + B + C == N and A % 2 == 0 and C >= B + 2:
                result += 1

print(result)