import sys
input = sys.stdin.readline

a = int(input())
mamber = []
for i in range(a):
    age, name = input().split()
    mamber.append((int(age), name))
mamber.sort(key = lambda x : x[0])
for age, name in mamber:
    print(age, name)