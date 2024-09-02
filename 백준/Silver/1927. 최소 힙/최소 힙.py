import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        # 배열에 x라는 값을 넣는 연산
        heapq.heappush(heap, x)
    else:
        # 배열에서 가장작은 값을 출력하고 그 값을 배열에서 제거
        # 비어있으면 0 출력
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)