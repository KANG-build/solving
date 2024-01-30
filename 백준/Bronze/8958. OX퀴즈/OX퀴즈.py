SUM = 0
ST = 0
a = int(input())
for i in range(a):
    b = input()
    for i in b:
        if i == 'O':
            ST += 1
        elif i == 'X':
            SUM += sum(range(ST+1))
            ST = 0
    SUM += sum(range(ST+1))
    ST = 0
    print(SUM)
    SUM = 0
