import sys
input = sys.stdin.readline

# 팰린드롬을 판별식
def check(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

# 입력 받기
n = int(input())
count = 0

for _ in range(n):
    input_data = input().rstrip()
    if check(input_data):
        count += 1

# 팰린드롬 개수를 구한다
# 경우의 수를 구한다
## 한 쌍에 두개가 나온다
print(count * (count-1))