def solution(numbers):
    a = 0 
    for i in numbers:
        a += i
        answer = a / len(numbers)
    return answer