def solution(numbers):
    # 모든 조합을 만들어(2중 순회 O(N^2)) 오름차순 정렬(O(NlogN))
    # 최대 길이 100이하 100^2 = 10000
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            
    return sorted(set(answer))