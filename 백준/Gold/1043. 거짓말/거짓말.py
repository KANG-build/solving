def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]  # 0은 안 쓰는 값
party = []
truth = list(map(int, input().split()))
answer = 0

for i in truth[1:]:
    parent[i] = 0

for i in range(m):
    input_data = list(map(int, input().split()))
    party.append(input_data[1:])
    for j in range(2, input_data[0]+1):
        union_parent(parent, parent[input_data[j-1]], parent[input_data[j]])

for i in party:
    if 0 not in [find_parent(parent, parent[j]) for j in i]:
        answer += 1
    
print(answer)