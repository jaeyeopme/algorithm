import sys

input = sys.stdin.readline

T = int(input())
S = [input().strip() for _ in range(T)]
ans = []

for s in S:
    left_diff = 0
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        if s[left + 1] == s[right]:
            left += 1
            left_diff += 1
        elif s[left] == s[right - 1]:
            right -= 1
            left_diff += 1
        else:
            left_diff = 2
            break

    right_diff = 0
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        if s[left] == s[right - 1]:
            right -= 1
            right_diff += 1
        elif s[left + 1] == s[right]:
            left += 1
            right_diff += 1
        else:
            right_diff = 2
            break

    v = min(left_diff, right_diff)
    ans.append(v if v < 2 else 2)

print(*ans)
