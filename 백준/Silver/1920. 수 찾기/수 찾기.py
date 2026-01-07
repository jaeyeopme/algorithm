import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

[print(1 if t in A else 0) for t in T]
