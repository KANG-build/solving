def solution(n):
    count_one = str(bin(n)).count('1')
    
    while True:
        n += 1
        if str(bin(n)).count('1') == count_one:
            return n
        
    return n