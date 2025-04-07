def solution(numbers):
    answer = ''.join(list(reversed(sorted([str(i) for i in numbers], key=lambda x : str(x)*3))))
    return str(int(answer))