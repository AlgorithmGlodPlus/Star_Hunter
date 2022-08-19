# 부족한 금액 계산하기
# Level 1
def solution(price, money, count):
    answer = -1
    total = 0

    for i in range(count):
        total += price * (i+1)

    answer = (total - money) if total - money > 0 else 0
    return answer