import sys
from collections import defaultdict

input = sys.stdin.readline

N, C = map(int, input().split())
M = list(map(int, input().split()))

m_count = defaultdict(int)

for m in M:
    m_count[m] += 1

for m in sorted(m_count.keys(), key=lambda x: m_count[x], reverse=True):
    for _ in range(m_count[m]):
        print(m, end=' ')
