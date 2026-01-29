import sys

input = sys.stdin.readline

def check():
  global M, current, ans
  if current['A'] >= M[0] and current['C'] >= M[1] and \
      current['G'] >= M[2] and current['T'] >= M[3]:
    ans += 1


S, P = map(int, input().split())
DNA = input().rstrip()
M = list(map(int, input().split()))
ans = 0

start, end = 0, P - 1
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 초기 값 설정
for i in range(start, end + 1):
  current[DNA[i]] += 1

check()

while end < S - 1:
  # 우측으로 이동
  current[DNA[start]] -= 1
  start += 1
  end += 1
  current[DNA[end]] += 1

  check()

print(ans)
