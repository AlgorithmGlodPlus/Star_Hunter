import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = [0] * (N + 1)

for x in reversed(range(1, N + 1)):
    cal = []
    if x % 3 == 0:
        cal.append(x // 3)
    if x % 2 == 0:
        cal.append(x // 2)
    if x - 1 != 0:
        cal.append(x - 1)

    for nx in cal:
        if 1 <= nx < (N + 1):
            if nums[nx] == 0:
                nums[nx] = nums[x] + 1
            else:
                nums[nx] = min(nums[nx], nums[x] + 1)

print(nums[1])
