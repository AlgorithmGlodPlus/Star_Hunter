import sys
from collections import deque


def bfs(n, m, box):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    # 박스에 토마토가 들어있는 위치 큐에 삽입
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])



def solution(n, m, box):
    answer = 0

    bfs(n, m, box)

    for i in box:
        for j in i:
            if j == 0:
                return -1
        answer = max(answer, max(i))

    return answer - 1


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().rstrip().split())
    box = [list(map(int, input().rstrip().split())) for _ in range(m)]

    print(solution(n, m, box))