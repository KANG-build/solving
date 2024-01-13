def solution(polynomial):
    a = 0
    b = 0
    for i in polynomial.split(' + '):
        if 'x' in i:
            if i == 'x':
                a += 1
            else: a += int(i[:-1])
        else:
            b += int(i)
    
    if b:
        if a:
            if a == 1:
                return f"x + {b}"
            return f"{a}x + {b}"
        else: 
            return f"{b}"
    else:
        if a:
            if a == 1:
                return f"x"
            return f"{a}x"
        else: return '0'