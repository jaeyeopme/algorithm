N, Q = map(int, input().split())
X = list(map(int, input().split()))
P = [int(input()) for _ in range(Q)]

X.sort()

for p in P:
    start, end = 0, N - 1

    while start != end:
        mid = (start + end) // 2

        # p보다 큰 좌표 찾기
        if X[mid] > p:
            end = mid
            continue
        # p보다 커야 하기 때문에 시작 값은 mid + 1 로
        start = mid + 1

    # p는 X[start - 1], X[start] 사이에 있음
    if start != 0 and abs(p - X[start - 1]) <= abs(p - X[start]):
        print(X[start - 1])
        continue

    print(X[start])
