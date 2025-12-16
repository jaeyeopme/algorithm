import sys

input = sys.stdin.readline
N, B = map(int, input().split())

result = []

while N >= B:
    result.append(N % B)
    N //= B
result.append(N)

for i in reversed(result):
    print(chr(i + 55) if i > 9 else i, end="")
