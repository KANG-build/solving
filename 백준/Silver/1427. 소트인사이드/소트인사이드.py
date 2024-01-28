a = input()
print(''.join([str(j) for j in sorted([int(i) for i in a], reverse=True)]))