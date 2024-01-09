A = int(input())
B = int(input())
C = int(input())
D = A * B * C

for i in range(10):
    print(str(D).count(f'{i}'))