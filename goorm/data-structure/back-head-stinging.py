N = int(input())
H = list(map(int, input().split()))
stack = []

for h in H:
    # h를 볼 수 있는 좌측 봉우리 개수
    print(len(stack), end=" ")

    # h의 우측 봉우리를 볼 수 없는 h보다 작거나 같은 좌측 봉우리들을 제거
    while stack and stack[-1] <= h:
        stack.pop()

    # h는 우측 봉우리를 볼 수 있음
    stack.append(h)
