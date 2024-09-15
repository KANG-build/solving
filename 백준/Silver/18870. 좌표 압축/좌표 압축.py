import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
mapping = {}

# len(set(array))만큼 수가 나올것
for idx, num in enumerate(sorted(set(array))):
    mapping[str(num)] = idx
    
for i in array:
    print(mapping[str(i)], end=' ')