m = 0
m_x = 0
m_y = 0

a = 0
b = 0

for i in range(9):
    b += 1
    for j in input().split():
        a += 1
        if int(j) >= m:
            m = int(j)
            m_x = a
            m_y = b
    a = 0
    
print(m)
print(m_y, m_x)