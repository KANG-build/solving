hmm = {}
answer = 0
result = 0
while True:
    inp = input().split()
    if inp[0] == '-1':
        break
    
    if inp[2] == 'wrong':
        if inp[1] in hmm:
            hmm[inp[1]] += 1
        else:
            hmm[inp[1]] = 1
    elif inp[2] == 'right':
        answer += 1
        result += int(inp[0])
        if inp[1] in hmm:
            result += hmm[inp[1]] * 20
            
print(answer, result)    

    