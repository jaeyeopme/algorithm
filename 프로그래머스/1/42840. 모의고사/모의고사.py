def solution(answers):
    answer = {1: 0, 2: 0, 3: 0}
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for a in answers:
        f = first.pop(0)
        first.append(f)
        s = second.pop(0)
        second.append(s)
        t = third.pop(0)
        third.append(t)

        if f == a:
            answer[1] += 1
        if s == a:
            answer[2] += 1
        if t == a:
            answer[3] += 1
    
    arr = sorted(answer.keys(), key=lambda k: answer[k], reverse=True)
    top = arr[0]
    
    return [current for current in arr if answer[top] == answer[current]]
