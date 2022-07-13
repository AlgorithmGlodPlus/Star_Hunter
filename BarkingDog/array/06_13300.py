import sys
import math

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
students = [[0, 0] for _ in range(7)]
for i in range(N):
    S, Y = map(int, input().rstrip().split())
    students[Y][S] += 1

answer = 0
for f, m in students:
    if f != 0:
        answer += math.ceil(f/K)

    if m != 0:
        answer += math.ceil(m/K)

print(answer)