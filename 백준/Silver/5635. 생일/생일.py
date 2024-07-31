n = int(input())
person = []
for i in range(n):
    name, d, m, y = map(str, input().split())
    person.append([name, int(d), int(m), int(y)])

new = sorted(person, key=lambda x:(x[3], x[2], x[1]))
print(new[-1][0])
print(new[0][0])