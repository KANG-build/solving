a = int(input())
HG = {}
for i in range(a):
    inp = input().split()
    if inp[0] in HG:
        HG[inp[0]] += (int(inp[1]))
    else:
        HG[inp[0]] = (int(inp[1]))

flag = 0
for i in HG:
    if HG[i] == 5:
        flag = 1
        
if flag == 1:
    print('YES')
else:
    print('NO')