# 다시 풀어보기
# 점화식 구하기
import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]

def func(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return func(num-1) + func(num-2) + func(num-3)


for num in nums:
    print(func(num))


