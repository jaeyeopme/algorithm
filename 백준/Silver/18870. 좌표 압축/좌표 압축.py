import sys

input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))

sorted_x, x_count = sorted(set(X)), {}

for i in range(len(sorted_x)):
    value = sorted_x[i]
    x_count[value] = i

for x in X:
    print(x_count[x], end=' ')
