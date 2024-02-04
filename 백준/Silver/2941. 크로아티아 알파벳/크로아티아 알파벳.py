import sys
input = sys.stdin.readline

s = input().strip()
TWO = s.count('c=') + s.count('c-') + s.count('d-') + s.count('lj') + s.count('nj') + s.count('s=') + s.count('z=')
TWR = s.count('dz=')
print(len(s) - TWO - TWR)
