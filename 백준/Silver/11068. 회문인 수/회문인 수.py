import sys

input = sys.stdin.readline

TC = [int(input()) for _ in range(int(input()))]

for T in TC:
    isPalindrome = False

    # B 진법
    for B in range(2, 65):
        N, arr = T, []

        while N >= B:
            arr.append(N % B)
            N //= B
        arr.append(N)

        if arr == arr[::-1]:
            isPalindrome = True

    print(int(isPalindrome))