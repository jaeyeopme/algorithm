import sys

input = sys.stdin.readline

n = int(input())
na = [False] * 1000001

a = sorted(list(map(int, input().split())))
x = int(input())
count = 0

# 1000000
for i in a:
    na[i] = True

for i in a:
    j = x - i

    if i < j <= 1000001 and na[j]:
        count += 1
        na[j] = False

print(count)
