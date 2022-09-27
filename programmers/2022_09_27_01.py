# 타겟 넘버
# Level 2
def solution(numbers, target):
    sup = [0]

    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)
        sup = sub

    return sup.count(target)