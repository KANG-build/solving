def solution(d, budget):
    i = 0
    while True:
        i += 1
        if sum(sorted(d)[:i]) > budget:
            return i-1
        if i == len(d):
            return i