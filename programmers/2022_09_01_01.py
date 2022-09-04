# 두 큐 합 같게 만들기
# Level 2
from collections import deque

def solution(queue1, queue2):
    answer = -1

    que1 = deque(queue1)
    que2 = deque(queue2)

    sq1 = sum(que1)
    sq2 = sum(que2)
    total = (sq1 + sq2) // 2

    # while문 사용시 무한 루프 도는 케이스 발생 -> for문으로 범위 줘서 해결
    for i in range(len(queue1) * 3):
        if sq1 == total:
            return i
        elif sq1 > total:
            t = que1.popleft()
            sq1 -= t
            sq2 += t
            que2.append(t)
        else:
            t = que2.popleft()
            sq1 += t
            sq2 -= t
            que1.append(t)

    return answer