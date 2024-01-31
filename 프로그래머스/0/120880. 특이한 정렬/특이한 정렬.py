def solution(numlist, n):
    temp = 0
    for i in range(len(numlist)-1):
        for j in range(len(numlist)-1):
            if abs(numlist[j]-n) > abs(numlist[j+1]-n):
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
            if abs(numlist[j]-n) == abs(numlist[j+1]-n):
                if numlist[j] < numlist[j+1]:
                    temp = numlist[j]
                    numlist[j] = numlist[j+1]
                    numlist[j+1] = temp
    return numlist