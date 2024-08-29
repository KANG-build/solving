import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
tree = list(map(int, input().split()))

# start, end
start = 0 
end = max(tree)

# 이진탐색 구현
result = 0
while start <= end:
    mid = (start + end) // 2
    # 잘린 나무 체크
    total = 0
    for i in tree:
        if i > mid:
            total += i-mid
    
    # 왼쪽 확인 (나무 부족) 
    if total < m:
        end = mid - 1 
    # 오른쪽 확인 (나무 충분)
    else: 
        result = mid
        start = mid + 1

print(result)