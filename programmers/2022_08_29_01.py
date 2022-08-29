# 정수 제곱근 판별
# Level 1
import math

def solution(n):
    answer = -1

    for i in range(int(math.sqrt(n)) + 1):
        if i * i == n:
            answer = (i+1) * (i+1)
            break

    return answer