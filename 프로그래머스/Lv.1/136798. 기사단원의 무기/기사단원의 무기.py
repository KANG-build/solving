def solution(number, limit, power):
    hap = 0
    steel = 0
    for i in range(1, number+1):
        # 제곱근 n까지만 계산해서 시간을 줄인다
        for j in range(1, int((i)**0.5)+1):
            if j == (i**0.5):
                hap += 1
            elif i % j == 0:
                hap += 2
            if hap > limit:
                break
                
        if hap > limit:
            steel += power
        else: steel += hap
        hap = 0
    return steel