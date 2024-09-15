import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_data = list(map(int, input().split()))
array = [0] * (n+1) 
save = 0

for idx, num in enumerate(input_data):
    save += num
    array[idx+1] = save

for i in range(m):
    a, b = map(int, input().split())
    print(array[b] - array[a-1], end=' ')