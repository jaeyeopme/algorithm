def solution(s):
    answer = 0
    stack = []
    
    for c in s:
        # 비어있지 않을 때
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    if not stack:
        answer = 1
        
    return answer