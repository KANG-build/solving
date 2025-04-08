import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    # 두 개 빼고 섞은 걸 다시 넣는다 (k 이상인지 체크)
    while scoville[0] < K: 
        if len(scoville) == 1:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        count += 1

    return count