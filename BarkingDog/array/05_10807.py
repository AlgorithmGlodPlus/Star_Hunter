import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
v = int(input().rstrip())

print(nums.count(v))