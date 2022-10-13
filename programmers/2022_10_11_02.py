# 행렬 테두리 회전하기
# Level 2
def solution(rows, columns, queries):
    answer = 0
    count = 0
    matrix = [ [0] * columns for i in range(rows)]

    for i in range(columns):
        for j in range(rows):
            count += 1
            matrix[i][j] = count

    for sx, sy, ex, ey in queries:
        print(sx, sy, ex, ey)


    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))