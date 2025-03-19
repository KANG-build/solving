def solution(players, callings):
    # 해시를 둘 다 만든다ㄷㄷㄷㄷ
    idx_dic = {}
    name_dic = {}
    for idx, name in enumerate(players):
        idx_dic[idx+1] = name
        name_dic[name] = idx+1

    for name in callings:
        save = idx_dic[name_dic[name]-1]

        # (1) 이름을 바꿔줘야 한다
        idx_dic[name_dic[name]], idx_dic[name_dic[name]-1] = idx_dic[name_dic[name]-1], idx_dic[name_dic[name]]
        # (2) 순위를 바꿔줘야 한다
        name_dic[name], name_dic[save] = name_dic[save], name_dic[name]
    
    return [i[1] for i in idx_dic.items()]