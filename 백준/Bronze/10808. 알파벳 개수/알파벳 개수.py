import sys
input = sys.stdin.readline

alp = [chr(i) for i in range(ord('a'), ord('z')+1)]
answer = [0 for i in range(26)]

s = input().strip()
for i in s:
    answer[alp.index(i)] += 1

for i in answer:    
    print(i, end=' ')