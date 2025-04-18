import bisect

N = int(input())
S = list(map(int, input().split()))
ans = 0

S.sort()

# 오름차순으로 선택하여 동일한 요소 집합이 중복되지 않도록 제한
for i in range(N - 2):  # k에서 먼저 N에 도달함
    for j in range(i + 1, N - 1):
        # S[k] <= S[i] + S[j]
        # k가 될 수 있는 값의 범위는 S[j + 1] 부터 S[i] + S[j] 를 만족하는 위치까지
        # S[i] + S[j]를 만족하는 위치를 포함해야하기 때문에 -1
        end_k = bisect.bisect_right(S, S[i] + S[j]) - 1
        # k가 될 수 있는 값의 범위는 j + 1 부터 end_k 까지임
        ans += (end_k - j + 1) - 1

print(ans)
