def solution(my, queries):
    for s, e in queries:
        my = ''.join([my[:s], my[s:e+1][::-1], my[e+1:]])
    return my