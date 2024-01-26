def solution(lottos, win_nums):
    cor = []
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                cor.append(lotto)
    if 0 in lottos or cor:
        return [max(1, 7-lottos.count(0)-len(cor)), min(6, 7-len(cor))]
    else:
        return [6, 6]