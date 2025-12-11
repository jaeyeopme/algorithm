import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
