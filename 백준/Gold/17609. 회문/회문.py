import sys

input = sys.stdin.readline


def is_palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def solve(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        check_left = is_palindrome(s, left + 1, right)
        check_right = is_palindrome(s, left, right - 1)

        if check_left or check_right:
            return 1
        else:
            return 2

    return 0


for _ in range(int(input())):
    s = input().strip()
    print(solve(s))
