import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
prefix_sum, answer = [0], 0

for a in A:
    prefix_sum.append(prefix_sum[-1] ^ a)

for _ in range(Q):
    s, e = map(int, input().split())
    xor = prefix_sum[e] ^ prefix_sum[s - 1]
    answer ^= xor

print(answer)
