n = int(input())
answer = []

def hanoi_tower(n, start, temp, end):
    if n == 1:
        print(start, end)
    else:
        hanoi_tower(n-1, start, end, temp)
        print(start, end)
        hanoi_tower(n-1, temp, start, end)
        

if n > 20:
    print(2**n -1)
else:
    print(2**n -1)
    hanoi_tower(n, '1', '2', '3')