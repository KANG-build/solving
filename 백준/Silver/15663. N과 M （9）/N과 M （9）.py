import sys
import heapq
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
heap = []

for i in set(permutations(num, M)):
    heapq.heappush(heap, i)

for i in range(len(heap)):
    for j in heapq.heappop(heap):
        print(j, end=' ')
    print()