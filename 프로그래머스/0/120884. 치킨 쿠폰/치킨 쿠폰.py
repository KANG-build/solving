def solution(chicken):
    result = 0
    ticket = 0
    while True:
        result += chicken // 10
        ticket += chicken % 10
        chicken = chicken // 10
        
        if chicken < 10:
            result += (chicken+ticket)//10
            result +=  ((chicken+ticket)%10 + (chicken+ticket)//10)//10
            return result 