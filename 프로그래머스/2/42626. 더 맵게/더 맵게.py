import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) >= 2:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)

            if a >= K:
                return answer
            else:
                heapq.heappush(scoville, a+b*2)
                answer += 1
        else:
            if scoville[0] >= K:
                return answer
            else:
                return -1
                
    return -1