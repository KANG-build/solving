a, b = map(int, input().split())
box = [i for i in range(1, a+1)]

tmp = 0
for i in range(b):
    f, s = map(int, input().split())
    tmp = box[f-1:s]
    tmp.reverse()
    box[f-1:s] = tmp
    
for i in range(len(box)):
    print(box[i], end=' ')