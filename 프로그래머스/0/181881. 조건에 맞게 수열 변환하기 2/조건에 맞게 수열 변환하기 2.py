def solution(arr):
    answer = 0
    while True:
        save = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i]%2 == 1:
                arr[i] = 2*arr[i] + 1
            
        if save == arr:
            return answer
        
        answer += 1
        
    return 0