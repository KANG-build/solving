#######################
# 2667 단지번호붙이기 #
#######################


import sys
sys.setrecursionlimit(1000000)

def dfs(i, j):
    # 범위 체크
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    
    if graph[i][j] == 1:
        graph[i][j] = 0
        answer[number-1] += 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    else:
        return
    
n = int(input())
graph = []
answer = []

for i in range(n):
    graph.append(list(map(int, input())))  # 방문 가능 0

m = len(graph[0])

number = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            number += 1
            answer.append(0)
            dfs(i, j)

# 답 출력
print(len(answer))
for i in sorted(answer):
    print(i)