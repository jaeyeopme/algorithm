N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append((A[i], i + 1))  # 1 based

B.sort()

for day in range(N):
    t, n = B[day]
    if t - day <= 0:  # 0이 되는 경우 사전순으로 출력
        print(*[n for n in range(1, N + 1)])
        exit()

print(*[n for _, n in B])
