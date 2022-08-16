# 소수 만들기
# Level 1
import math

def solution(nums):
    answer = 0
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                n = nums[i] + nums[j] + nums[k]

                def is_prime(num):
                    for m in range(2, int(math.sqrt(num) + 1)):
                        if num % m == 0:
                            return False
                    return True

                if is_prime(n):
                    answer += 1

    return answer

print(solution([1, 2, 3, 4]))