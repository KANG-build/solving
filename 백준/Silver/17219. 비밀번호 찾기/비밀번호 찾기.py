import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ID = {}
for i in range(a):
    site, pw = map(str, input().split())
    ID[site] = pw
for i in range(b):
    site = input().strip()
    print(ID.get(site))