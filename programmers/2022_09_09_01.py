# 멀쩡한 사각형
# Level 2

# 수학문제
# 좌표 상에서 가로, 세로의 최대 공약수를 이용하여 푸는 문제
import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w,h))