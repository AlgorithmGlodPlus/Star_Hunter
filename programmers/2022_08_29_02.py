# 제일 작은 수 제거하기
# Level 1
def solution(arr):
    answer = []

    if len(arr) == 1:
        answer.append(-1)
    else:
        n = min(arr)
        for i in range(len(arr)):
            if arr[i] == n:
                del arr[i]
                break
        answer = arr
    return answer