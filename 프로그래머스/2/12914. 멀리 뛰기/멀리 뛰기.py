def solution(n):
    # 각 칸에 도달하는 방법의 수를 저장할 리스트 초기화
    # 첫 번째 칸에 도달하는 방법은 1가지, 두 번째 칸에 도달하는 방법은 2가지이므로 초기값 설정
    ways = [0] * (n+1)
    ways[1] = 1
    if n > 1:
        ways[2] = 2
    
    # 3번째 칸부터 n번째 칸까지 각 칸에 도달하는 방법의 수 계산
    for i in range(3, n+1):
        ways[i] = (ways[i-1] + ways[i-2]) % 1234567
    
    return ways[n]