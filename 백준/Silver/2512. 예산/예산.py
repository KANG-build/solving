##############
# 2512. 예산 #
##############

import sys
# input = sys.stdin.readline

# 입력 받기
n = int(input())
array = list(map(int, input().split()))
m = int(input())

# start, end
start = 1
end = max(array)

# 이진탐색 구현
result = 0
while start <= end:
    mid = (start + end) // 2
    # 잘린 나무 체크
    total = 0
    for i in array:
        if i < mid:
            total += i
        else:
            total += mid
    
    # 왼쪽 확인
    if total > m:
        end = mid - 1 
    # 오른쪽 확인 
    else:
        result = mid
        start = mid + 1

print(result)