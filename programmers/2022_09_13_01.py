# 124 나라의 숫자
# Level 2

def solution(n):
    answer = ''

    if n < 3:
        return str(n)
    else:
        thr = digit(n)
        for i in reversed(range(1, len(thr))):
            if thr[i] == 0:
                thr[i] = 4
                for j in reversed(range(i)):
                    if thr[j] == 0:
                        thr[j] = 2
                    elif thr[j] == 4:
                        thr[j] = 2
                        break
                    else:
                        thr[j] -= 1
                        break

        for i in range(len(thr)):
            if i == 0 and thr[i] == 0:
                continue
            else:
                answer += str(thr[i])

        return answer


# 3진법 계산
def digit(n):
    thr = []

    r = 0
    while n > 2:
        r = n % 3
        n //= 3
        thr.append(r)
    thr.append(n)

    thr.reverse()
    return thr
