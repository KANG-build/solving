a = int(input())
A = []
for i in range(a):
    num = int(input())
    A.append(num)

for i in sorted(A):
    print(i)