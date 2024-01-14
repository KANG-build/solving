def solution(left, right):
    count = 0
    sum = 0   
    for n in range(left, right+1):
        for i in range(1, n+1):
            if n%i==0:
                count += 1
        print(count)        
        if count%2:
            sum -= n
        else: sum += n
        count = 0
    return sum
