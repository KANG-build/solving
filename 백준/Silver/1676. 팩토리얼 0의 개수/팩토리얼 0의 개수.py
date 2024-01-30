num = 1
count = 0

a = int(input())
for i in range(1, a+1):
    num *= i
for j in reversed(str(num)):
    if j != '0':
        break
    count += 1
    
print(count)