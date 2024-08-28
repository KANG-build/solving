##############
# 7568. 덩치 #
##############

n = int(input())
array = []

# 초기 설정
for i in range(n):
    kg, cm = map(int, input().split())
    array.append([kg, cm, 1])
    
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다
for i in range(len(array)):
    for j in range(i, len(array)):
        # 몸무게 판정
        if array[i][0] > array[j][0]:
            if array[i][1] > array[j][1]:
                array[j][2] += 1
        elif array[i][0] < array[j][0]:
            if array[i][1] < array[j][1]:
                array[i][2] += 1
                
for i in array:
    print(i[2], end=' ')