# x만큼 간격의 있는 n개의 숫자
# Level 1
def solution(x, n):
    answer = []
    s = 0
    for i in range(n):
        s += x
        answer.append(s)
    return answer