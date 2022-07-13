import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

ascii_1 = [0] * 26
ascii_2 = [0] * 26

for s in str1:
    ascii_1[ord(s) - 97] += 1

for s in str2:
    ascii_2[ord(s) - 97] += 1

answer = 0
for i in range(26):
    if ascii_1[i] > 0 or ascii_2[i] > 0:
        if ascii_1[i] != ascii_2[i]:
            answer += abs(ascii_1[i] - ascii_2[i])

print(answer)