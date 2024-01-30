a = input()
a = a.upper()
ct = []
alp = [chr(i) for i in range(ord('A'), ord('Z')+1)]

for i in range(ord('A'), ord('Z')+1):
    ct.append(a.count(chr(i)))

if ct.count(max(ct)) > 1:
    print('?')
else:
    print(alp[ct.index(max(ct))])