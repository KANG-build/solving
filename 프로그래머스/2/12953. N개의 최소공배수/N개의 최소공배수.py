import math 

def solution(arr):
    for i in range(1, len(arr)):
        arr[i] = int(arr[i]*arr[i-1] / math.gcd(arr[i], arr[i-1]))
    return arr[-1]