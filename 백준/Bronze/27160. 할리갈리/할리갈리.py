a = int(input())
HG = {}
for i in range(a):
    inp = input().split()
    if inp[0] in HG:
        HG[inp[0]] += (int(inp[1]))
    else:
        HG[inp[0]] = (int(inp[1]))

for i in HG:
    if HG[i] == 5:
        print('YES')
        exit()

print('NO')