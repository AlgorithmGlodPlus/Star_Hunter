# 124 나라의 숫자
# Level 2

def solution(n):
    answer = ''
    re = [4]
    t = n // 3

    while t > 3:
        t //= 3
        r = t % 3
        re.append(r)


    return answer
