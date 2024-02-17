N = int(input())

for _ in range(N):
    S = int(input())
    
    for i in range(2, 1_000_001):
        if S % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
            break