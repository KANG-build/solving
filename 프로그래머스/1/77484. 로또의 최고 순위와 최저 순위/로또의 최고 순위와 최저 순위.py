def solution(lottos, win_nums):
    cor = 0
    for lotto in lottos:
        if lotto in win_nums:
            cor += 1
    if 0 in lottos or cor:
        return [max(1, 7-lottos.count(0)-cor), min(6, 7-cor)]
    else:
        return [6, 6]