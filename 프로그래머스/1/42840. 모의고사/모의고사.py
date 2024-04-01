def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0] * 3
    
    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            # pattern 을 answers 의 길이만큼 반복해야하기 때문에 나머지 연산이 필요함
            if a == p[i % len(p)]:
                scores[j] += 1
    
    max_score = max(scores)
    
    answer = []
    for i, score in enumerate(scores):
        if max_score == score:
            answer.append(i + 1)
    
    return answer 
    