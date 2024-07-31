N, M = map(int, input().split())
ball = [i+1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    ball[a-1], ball[b-1] = ball[b-1], ball[a-1]

for i in ball:
    print(i, end=' ')