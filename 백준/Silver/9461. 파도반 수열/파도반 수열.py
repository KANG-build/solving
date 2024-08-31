#####################
# 9461. 파도반 수열 #
#####################

t = int(input())
d = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(t):
    n = int(input())
    
    if n < len(d):
        print(d[n-1])
    else:
        for i in range(len(d), n):
            d.append(d[i-1] + d[i-5])
        print(d[-1])