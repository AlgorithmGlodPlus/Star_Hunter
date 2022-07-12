import sys

input = sys.stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())

mul = str(A * B * C)
answer = [0] * 10

for i in mul:
    answer[int(i)] += 1

for i in answer:
    print(i)
