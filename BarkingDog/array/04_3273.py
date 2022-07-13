import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
x = int(input().rstrip())

result = [0] * 2000001

for num in nums:
    aj = x - num
    if aj > 0:
        result[aj] = 1

for num in nums:
    aj = x - num
    if result[num] == 1:
        result[num] += 1
        result[aj] -= 1

print(result.count(2))