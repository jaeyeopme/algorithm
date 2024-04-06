def solution(s):
    answer = 0
    bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for _ in range(len(s)):
        s = s[1:] + s[0]
        stack = []
        
        for c in s:
            if c in bracket.values():
                stack.append(c)
                continue
            elif not stack or bracket[c] != stack.pop():
                break
        else:
             if not stack:
                answer += 1

    return answer