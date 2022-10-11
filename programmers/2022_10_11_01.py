# 짝지어 제거하기
# Level 2
def solution(s):
    answer = 0
    stack_1 = list(s)
    stack_2 = []

    while len(stack_1) > 1:
        r = stack_1.pop()
        if r == stack_1[-1]:
            stack_1.pop()
            if stack_2:
                stack_1.append(stack_2.pop())
        else:
            stack_2.append(r)

    if not stack_1 and not stack_2:
        answer = 1

    return answer


print(solution('a'))