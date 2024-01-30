a = int(input())
for i in range(a):
    floor, room, guest = map(int, input().split())
    # 층 출력
    if guest%floor == 0:
        print(floor, end='')
    else: print(guest%floor, end='')
    
    # 방 출력

    if guest//floor + 1 < 10:
        if guest%floor == 0:
            print(0, end='')
            print(guest//floor)
        else:
            print(0, end='')
            print(guest//floor + 1)
    else: 
        if guest%floor == 0:
            if guest//floor < 10:
                print(0, end='')
                print(guest//floor)
            else: print(guest//floor)
        else: print(guest//floor + 1)
    