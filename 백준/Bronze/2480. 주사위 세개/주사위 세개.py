money = 0
a, b, c = map(int, input().split())

if a == b == c :
    print(a * 1000 + 10000)
elif (a == b) and (b != c):
    print(1000 + a * 100)
elif (a == c) and (b != c):
    print(1000 + a * 100)
elif (b == c) and (a != c) :
    print(1000 + b * 100)
else:
    print(max([a, b, c]) * 100)