# 로또의 최고 순위와 최저 순위
# Level 1

def solution(lottos, win_nums):

    zeros = 0
    right = 0
    for l in lottos:
        if l == 0:
            zeros += 1
        else:
            if l in win_nums:
                right += 1

    if (zeros + right) == 0:
        return [6, 6]

    high = 7 - (zeros + right)
    low = 6 if zeros == 6 else 7 - right

    return [high, low]