def solution(prices):
    n = len(prices)
    answer = [0] * n
    i_stack = [0]
    
    for i in range(1, n):
        # 가격이 떨어졌다면 이전 인덱스의 값이 얼마나 가격을 유지했는지 계산
        while i_stack and prices[i] < prices[i_stack[-1]]:
            j = i_stack.pop()
            # 이전 인덱스의 유지 기간 = 현재 인덱스 - 이전 인덱스
            answer[j] = i - j
        # 떨어지지 않았다면 인덱스 추가
        i_stack.append(i)
    
    # 가격이 떨어지지 않은 인덱스의 값이 얼마나 가격을 유지했는지 계산
    while i_stack:
        j = i_stack.pop()
        # 전체 기간 - 1 - 인덱스
        answer[j] = n - 1 - j
            
    return answer