# 올바른 괄호
# Level 2


def solution(s):
    answer = True
    stack = []

    if s[0] == ')':
        return False

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False

    return answer

