def solution(phone_book):
    # 해시 맵을 만들자 
    
    hash_map = {}
    for num in phone_book:
        hash_map[num] = 0
        
    for num in phone_book:
        seach_key = ''
        for i in num:
            seach_key += i
            if seach_key in hash_map and seach_key != num:
                return False
        
    return True