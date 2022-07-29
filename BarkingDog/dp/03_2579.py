import sys

input = sys.stdin.readline

n = int(input().rstrip())

steps = [0]
for _ in range(n):
    steps.append(int(input().rstrip()))

if n == 1:
    print(steps[1])
else:
    score = [0] * (n + 1)
    score[1] = steps[1]
    score[2] = steps[1] + steps[2]

    # 선택된 계단에서 1단계 아래와 2단계 아래의 계단 중 큰 값 선택
    for i in range(3, n + 1):
        score[i] = max(score[i-3] + steps[i-1] + steps[i], score[i-2] + steps[i])

    print(score[n])