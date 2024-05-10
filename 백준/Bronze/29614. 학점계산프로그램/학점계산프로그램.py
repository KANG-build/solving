s = 0
a = input()
for i in range(len(a)):
    if a[i] == '+':
        s += 0.5
    elif a[i] == 'A':
        s += 4.0
    elif a[i] == 'B':
        s += 3.0
    elif a[i] == 'C':
        s += 2.0
    elif a[i] == 'D':
        s += 1.0
        
print(s/(len(a)-a.count('+')))