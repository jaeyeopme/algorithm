def solution(numbers):
    size = len(numbers)
    answer = [numbers[i] + numbers[j] for i in range(size - 1) for j in range(i + 1, size)]
    
    return sorted(set(answer))