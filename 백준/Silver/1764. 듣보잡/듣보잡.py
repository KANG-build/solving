import sys
input = sys.stdin.readline

a, b = map(int, input().split())
listen = []
watch = []
for i in range(a):
    person = input().strip()
    listen.append(person)
for i in range(b):
    person = input().strip()
    watch.append(person)

Unheard = sorted(list(set(listen)&set(watch)))
print(len(Unheard))
for i in Unheard:
    print(i)