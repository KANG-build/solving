def solution(park, routes):
    # 'S'로 위치 설정
    h, w = 0, 0
    for i in range(len(park)):
        if 'S' in park[i]:
            h = i
            for j in range(len(park[i])):
                if park[i][j] == 'S':
                    w = j

                    
    # E, W, S, N에 따른 이동 방향
    dh = {'E':0, 'W':0, 'S':1, 'N':-1}
    dw = {'E':1, 'W':-1, 'S':0, 'N':0}
    
    # 이동 계획을 하나씩 확인
    for r in routes:
        m, n = r.split(' ')
        flag = True
        
        for i in range(int(n)+1):
            # 이동 후 좌표 구하기
            nh = h + dh[m] * i
            nw = w + dw[m] * i

            # 공간을 벗어나는 경우 무시
            if nh < 0 or nw < 0 or nh >= len(park) or nw >= len(park[0]):
                flag = False

            # 장애물이 있을 경우 무시
            elif park[nh][nw] == "X":
                flag = False

        # 이동 수행
        if flag:
            h, w = nh, nw

    return [h, w]