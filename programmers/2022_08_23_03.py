# 이상한 문자 만들기
# Level 1
def solution(s):
    answer = ''

    i = 0
    for w in s:
        if w == " ":
            answer += " "
            i = 0
        else:
            if i % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()
            i += 1

    return answer