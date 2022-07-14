##### 다시 풀어보기

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
answer = 0

nums = [0] * 100001
que = deque()
que.append(N)

while que:
    x = que.popleft()

    if x == K:
        answer = nums[x]
        break

    for i in (x+1, x-1, x*2):
        if 0 <= i <= 100000 and nums[i] == 0:
            nums[i] = nums[x] + 1
            que.append(i)

print(answer)