# 음양 더하기
# Level 1
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] * (1 if signs[i] else -1)
    return answer