def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    count = 0
    while not is_prime(a - count):
        count += 1
    print(count)
