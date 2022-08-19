# 2016
# Level 1
def solution(a, b):
    answer = ''
    day = 0
    x = [1, 3, 5, 7, 8, 10, 12]
    y = [4, 6, 9, 11]
    dow = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    for i in range(1, a):
        if i == 2:
            day += 29
        elif i in x:
            day += 31
        elif i in y:
            day += 30

    day += b

    answer = dow[day % 7 - 1]

    return answer