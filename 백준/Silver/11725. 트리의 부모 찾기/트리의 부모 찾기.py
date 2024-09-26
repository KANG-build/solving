import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def tree(parent_node, number):
    for i in array[number]:
        if i != parent_node:
            parent[i] = number
            tree(number, i)
    return

n = int(input())
array = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

parent = [0] * (n+1)
# 1번은 자식노드 2개
# 1의 자식노드(4, 6)로 가보면 1 빼고 다 손자임
tree(0, 1)

# 2번부터 부모와 자식이 들어있음
for i in parent[2:]:
    print(i)