# 체육복
# Level 1
def solution(n, lost, reserve):
    answer = 0
    st = [0 for i in range(n)]

    for l in lost:
        st[l-1] -= 1

    for r in reserve:
        st[r-1] += 1

    if st[0] == -1 and st[1] == 1:
        st[0], st[1] = 0, 0

    for i in range(1, n-1):
        if st[i] == -1:
            if st[i-1] == 1:
                st[i], st[i-1] = 0, 0
            elif st[i+1] == 1:
                st[i], st[i+1] = 0, 0

    if st[n-1] == -1 and st[n-2] == 1:
        st[n-1], st[n-2] = 0, 0

    for s in st:
        if s > -1:
            answer += 1

    return answer