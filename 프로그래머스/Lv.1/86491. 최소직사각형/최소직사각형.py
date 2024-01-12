def solution(sizes):
    a = [[max(i), min(i)] for i in sizes]
    return max(list(zip(*a))[0]) * max(list(zip(*a))[1])