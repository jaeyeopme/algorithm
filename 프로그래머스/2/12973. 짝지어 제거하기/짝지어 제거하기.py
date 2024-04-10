def solution(s):
    answer = 0
    stack = []
    
    for c in s:
        # 비어있지 않은 경우
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    # 비어있는 경우
    if not stack:
        answer = 1
        
    return answer