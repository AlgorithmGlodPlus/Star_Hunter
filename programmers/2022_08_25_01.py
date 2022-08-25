# 자릿수 더하기
# Level 1
def solution(n):
    answer = 0

    ch = str(n)

    for c in ch:
        answer += int(c)

    return answer