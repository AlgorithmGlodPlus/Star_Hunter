# 정수 내림차순으로 배치하기
# Level 1
def solution(n):
    rnum = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(list(map(str, rnum))))