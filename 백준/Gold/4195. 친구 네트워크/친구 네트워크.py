import sys
input = sys.stdin.readline

def union_parent(parent, a, b):  # a와 b를 union
    a = find_parent(parent, a)
    b = find_parent(parent, b)   
    if a < b:
        parent[b] = a
        
    else:
        parent[a] = b
    
def find_parent(parent, x): 
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

t = int(input())
for _ in range(t):
    name = {}
    group = {}
    f = int(input())  # 친구 관계의 수
    parent = []
    count = 0
    
    for _ in range(f):
        a, b = input().split()
        temp = len(name)
        # 이름 -> 숫자 변환
        if a not in name:
            name[a] = count
            parent.append(count)
            count += 1
        if b not in name:
            name[b] = count
            parent.append(count)
            count += 1
            
        # 이미 같은 집합인지 확인
        if find_parent(parent, name[a]) == find_parent(parent, name[b]):  
            print(group[find_parent(parent, name[a])])
        else:
            c, d = find_parent(parent, name[a]), find_parent(parent, name[b])
            MAX, MIN = max(c, d), min(c, d)  # MAX가 min에 합쳐지는 쪽
            union_parent(parent, name[a], name[b])
            
            # 인물 2명 추가 (새로운 그룹 2명, 2 출력)
            if len(name) == temp + 2:
                group[MIN] = 2
                print(group[MIN])
            # 인물 1명 추가 (기존 그룹에 합함, 추가된 그룹 인원 수 출력)
            elif len(name) == temp + 1:
                group[MIN] += 1
                print(group[MIN])
            # 인물 0명 추가 (그룹과 그룹을 합함)
            elif len(name) == temp:
                # 그룹과 그룹을 합함
                if c != d:
                    group[MIN] += group[MAX]
                print(group[MIN])