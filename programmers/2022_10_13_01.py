# 메뉴 리뉴얼
# Level 2
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        ordersDict = {}
        ordersCombi = []
        for o in orders:
            ordersCombi.extend(list(combinations(o, c)))
        print(ordersCombi)

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))