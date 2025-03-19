
def solution(dirs):
    answer = 0
    dic = {'L':(-1, 0), 'U':(0, 1), 'R':(1, 0), 'D':(0, -1)}
    reverse_dic = {'L':'R', 'U':'D', 'R':'L', 'D':'U'}
    mapp = [[set() for i in range(11)] for j in range(11)]
    x, y = 5, 5
    for i in dirs:
        temp_x = x+dic[i][0]
        temp_y = y+dic[i][1]
        
        # 이동이 안되면 막는다
        if temp_x < 0 or temp_y < 0 or temp_x > 10 or temp_y > 10:
            print(x, y, "에서", i, '로의 이동이 막힘')
            continue
        
        # 원래 있던 곳에 역으로 오거나, 내가 갈 곳에 내 방향으로 왔는지
        if (reverse_dic[i] in mapp[y][x]):
            mapp[temp_y][temp_x].add(i)
        elif (i in mapp[temp_y][temp_x]):
            mapp[y][x].add(reverse_dic[i])
        else:
            mapp[y][x].add(reverse_dic[i])
            mapp[temp_y][temp_x].add(i)
            answer += 1
        x = temp_x
        y = temp_y
    
    return answer