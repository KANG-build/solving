student = [i for i in range(1, 31)]
ex = []

for i in range(28):
        tmp = int(input())
        ex.append(tmp)

answer = list(set(ex) ^ set(student))
for i in answer:
    print(i)