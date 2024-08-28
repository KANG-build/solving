########################
# 15688. 수 정렬하기 5 #
########################

import sys
input = sys.stdin.readline

# 초기 세팅

count = [0] * 10001

n = int(input())
for i in range(n):
    a = int(input())
    count[a] += 1

# 출력
for i in range(10001):
    for j in range(count[i]):
        print(i)