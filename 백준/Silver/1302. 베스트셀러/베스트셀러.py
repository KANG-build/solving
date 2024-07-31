from collections import Counter

N = int(input())
word = []
for i in range(N):
    a = input()
    word.append(a)
    
print(Counter(sorted(word)).most_common()[0][0])    