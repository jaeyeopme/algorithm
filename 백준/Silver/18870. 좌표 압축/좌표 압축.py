import sys

input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))

sorted_x = sorted(set(X))
x_count = {}

for i in range(len(sorted_x)):
    value = sorted_x[i]
    x_count[value] = i

for x in X:
    print(x_count[x], end=' ')
