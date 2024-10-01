# 왼쪽의 가장 가까운 나무를 제거해도 남은 리스트가 모두 왼쪽 
# 오른쪽의 가장 가까운 나무를 제거해도 남은 리스트가 모두 오른쪽
# my_point 기준으로 왼쪽 나무와 오른쪽 나무를 분리

import sys
import heapq
input = sys.stdin.readline

left_trash = []
right_trash = []
my_point = 0
answer = 0

n = int(input())

for _ in range(n):
    input_data = input().rstrip()
    
    if input_data.startswith('1'):
        op, num = map(int, input_data.split())
        # 쓰레기를 버린다
        if num < my_point:  # 왼쪽 나무에 버릴 경우
            heapq.heappush(left_trash, abs(num-my_point))
        elif num > my_point:  # 오른쪽 나무에 버릴 경우
            heapq.heappush(right_trash, abs(num-my_point))
        
    elif input_data.startswith('2'):
        left_move = 0
        right_move = 0
        while True:
            if not right_trash and not left_trash:  # 텅 비었을 때
                break
            elif (right_trash and not left_trash) or (right_trash and left_trash and (right_move + left_trash[0] - left_move > left_move +  right_trash[0] - right_move)):  # 오른쪽이 더 가깝거나 오른쪽만 남음
                answer += left_move +  (right_trash[0] - right_move)  # 왼쪽에 있다가 올 때랑 오른쪽에 있다가 올 때 고려
                move = heapq.heappop(right_trash)
                left_move = 0  # 왼쪽에서 있다 왔을때 효과
                right_move = move  # 오른쪽으로 더 이동했음
            elif (left_trash and not right_trash) or (right_trash and left_trash and (right_move + left_trash[0] - left_move  <= left_move +  right_trash[0] - right_move)):  # 왼쪽이 더 가깝거나 왼쪽만 남음, 같아도 좌표가 더 작은 왼쪽으로 감 
                answer += right_move + (left_trash[0]  - left_move)
                move = heapq.heappop(left_trash)
                right_move = 0
                left_move = move
                
        my_point = my_point + right_move - left_move  # 마지막 위치가 기존에서 얼마만큼 더 움직였는지로 위치 갱신
        
print(answer)