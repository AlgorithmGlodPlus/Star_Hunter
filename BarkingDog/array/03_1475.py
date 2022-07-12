import sys
import math

input = sys.stdin.readline

N = input().rstrip()
answer = 1
cards = [0] * 9

for i in N:
    if i == '9':
        i = '6'

    cards[int(i)] += 1

cards[6] = math.ceil(cards[6] / 2)

print(max(cards))