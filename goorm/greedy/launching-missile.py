# 유클리드 거리의 제곱
def dist(x, y):
    return x**2 + y**2


N = int(input())
events = []
total_time = 0  # 총 이동시간

for i in range(N):
    X, Y, T = map(int, input().split())
    cur_time = dist(X, Y) * 2  # 현재 이동거리

    total_time += cur_time

    events.append((T, 1))  # 출발 시간
    events.append((T + cur_time, 0))  # 도착 시간

# 이벤트를 시간 순으로 정렬하면 동시 비행 중인 미사일을 구할 수 있음
events.sort()

# 동시 비행 미사일 수, 최대 동시 비행 미사일 수
max_flying_count = flying_count = 0

for _, on in events:
    if on:  # 비행 시작
        flying_count += 1
    else:  # 비행 종료
        flying_count -= 1

    # 부스터의 최대 효율은 동시 비행 미사일 수가 가장 많은 시점에 발생
    max_flying_count = max(max_flying_count, flying_count)

# 부스터 사용으로 절약되는 시간은 해당 시점에 비행 중인 미사일 수와 동일
print(total_time - max_flying_count)
