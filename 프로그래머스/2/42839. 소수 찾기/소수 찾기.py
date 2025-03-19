import math
import itertools

# 소수를 구하는 함수
def check(n):
    if n <= 1:
        return False 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    # 한 글자씩 자른다 
    arr = list(map(int, list(numbers)))
    all_arr = []
    # 만들 수 있는 수를 구한다 
    for i in range(1, len(arr)+1):
        all_arr += list(itertools.permutations(arr, i))
    

    all_set = set()
    
    for num_arr in all_arr:
        num = ''.join(list(map(str, num_arr)))
        if (int(num) not in all_set) and check(int(num)):
            print(num + "에서 올랏다")
            answer += 1
        all_set.add(int(num))
    # 소수를 구한다
    return answer