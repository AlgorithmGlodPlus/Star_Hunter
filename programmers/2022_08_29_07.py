# 하샤드 수
# Level 1
def solution(x):
    answer = True
    xs = str(x)

    total = 0
    for s in xs:
        total += int(s)

    if x % total != 0:
        answer = False

    return answer