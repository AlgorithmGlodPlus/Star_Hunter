# 약수의 개수와 덧셈
# Level 1
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        count = count_num(i)
        if count%2 == 0:
            answer += i
        else:
            answer -= i

    return answer

def count_num(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    return count