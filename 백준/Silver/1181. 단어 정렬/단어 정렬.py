import sys
input = sys.stdin.readline

num = int(input())
wordlist = []
for i in range(num):
    a = input()
    wordlist.append(a)

for i in sorted(set(wordlist), key = lambda x : (len(x), x)):
    print(i, end='')    