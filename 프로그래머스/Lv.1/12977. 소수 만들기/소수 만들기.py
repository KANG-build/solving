def solution(nums):
    count = 0
    check = 0
    for num in [nums[i]+nums[j]+nums[k] for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums))]:
        for div in range(2, num):
            if num % div == 0:
                break
        else:
                count += 1
    return count 