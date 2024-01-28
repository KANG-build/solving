def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = [[a, b, c, d].count(i) for i in [a, b, c, d]]
        
    if len(set(dice)) == 1:
        return 1111 * int(dice[0])
    elif len(set(dice)) == 2:
        if 2 not in count:
            return (10 * dice[count.index(3)] + dice[count.index(1)])**2
        else:
            return (list(set(dice))[0] + list(set(dice))[1]) * abs(list(set(dice))[0] - list(set(dice))[1])        
    elif len(set(dice)) == 3:
        return dice[count.index(1)] * dice[count.index(1, count.index(1)+1)]
    else:
        return sorted(dice)[0]
    return dice