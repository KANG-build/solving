import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
numlist = [int(input()) for i in range(N)]

# 산술평균
print(round(sum(numlist)/N))

# 중앙값
sorted_list = sorted(numlist)
print(sorted_list[N//2])

# 최빈값
counter_list = Counter(sorted_list).most_common(2)

if len(counter_list) == 1:
    print(counter_list[0][0])
elif counter_list[0][1] > counter_list[1][1]:
    print(counter_list[0][0])
else:
    print(counter_list[1][0])

# 범위
print(sorted_list[-1]-sorted_list[0])