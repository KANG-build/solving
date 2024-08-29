#####################
# 1654. 랜선 자르기 #
#####################

import sys
input = sys.stdin.readline

# 남는 길이가 mid * m이면 된다
n, m = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

# start, end
start = 1
end = max(array)

# 이진탐색 구현
result = 0
while start <= end:
    mid = (start + end) // 2
    # 잘린 랜선 체크
    total = 0
    for i in array:
        if i >= mid:
            total += i//mid  # 잘라서 몇개가 나오는지
    
    # 왼쪽 확인 (랜선 부족)
    if total < m:  # 개수 부족하면 다시
        end = mid-1
    else:
        result = mid
        start = mid+1
        
print(result)