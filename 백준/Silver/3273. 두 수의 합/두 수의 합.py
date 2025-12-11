import sys

input = sys.stdin.readline

int(input())
a = set(map(int, input().split()))
x = int(input())

count = 0

for i in a:
    if x - i in a:
        count += 1

print(count // 2)
