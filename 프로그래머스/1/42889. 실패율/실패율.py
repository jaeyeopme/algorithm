def solution(N, stages):
    answer = {}

    for i in range(1, N + 1):
        a, b = 0, 0

        for j in stages:
            if i == j:
                a += 1
            if i <= j:
                b += 1
        
        answer[i] = b if b == 0 else a / b

    return [key for key, _ in sorted(answer.items(), key=lambda x: x[1], reverse=True)]