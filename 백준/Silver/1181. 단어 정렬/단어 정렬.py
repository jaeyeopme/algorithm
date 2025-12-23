import sys

input = sys.stdin.readline

N = int(input())
words = set(input().strip() for _ in range(N))

print(*sorted(words, key=lambda x: (len(x), x)), sep="\n")