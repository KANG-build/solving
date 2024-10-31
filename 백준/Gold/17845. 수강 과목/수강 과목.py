import sys
input = sys.stdin.readline

t, n = map(int, input().split())
study = []
bag = [0] * (t+1)

for _ in range(n):
    b, a = map(int, input().split())
    study.append([a, b])  # time, value 
    
for time, score in sorted(study, key=lambda x : x[0]):
    for idx in range(t, time-1, -1):
        bag[idx] = max(bag[idx], bag[idx-time] + score)
        
print(bag[t])
    