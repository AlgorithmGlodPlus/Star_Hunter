# 기능개발
# Level 2
import math


def solution(progresses, speeds):
    answer = []
    pre = 0
    count = 0

    for p, s in zip(progresses, speeds):
        day = math.ceil(((100-p) / s))
        if pre == 0:
            pre = day
            count = 1
            continue

        if day > pre:
            answer.append(count)
            pre = day
            count = 1
        else:
            count += 1

    answer.append(count)

    return answer

