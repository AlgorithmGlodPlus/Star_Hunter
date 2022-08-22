# 문자열 내림차순으로 배치하기
# Level 1
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)