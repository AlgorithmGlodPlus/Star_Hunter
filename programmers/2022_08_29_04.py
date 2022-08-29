# 최대공약수와 최소공배수
# Level 1
def solution(n, m):
    answer = []
    a, b = n, m

    # 유클리드 호제법
    # 최대공약수
    while b != 0:
        r = a % b
        a, b = b, r

    # 최소공배수
    c = (n * m) / a

    return [a, c]