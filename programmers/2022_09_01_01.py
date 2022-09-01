# 두 큐 합 같게 만들기
# Level 2
from collections import deque

def solution(queue1, queue2):
    answer = -1

    que1 = deque(queue1)
    que2 = deque(queue2)

    total = (sum(queue1) + sum(queue2)) // 2

    count = 0
    while que1 and que2:
        if sum(que1) == total:
            return count
        elif sum(que1) > total:
            que2.append(que1.popleft())
        else:
            que1.append(que2.popleft())
        count += 1

    return answer