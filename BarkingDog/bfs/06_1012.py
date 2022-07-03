import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    # 상하좌우에 그림이 있는지 확인하는 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append([x, y])
    matrix[x][y] = 0 # 시작점 방문처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # x, y좌표의 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0  # 방문했으면 0으로 변경
                queue.append([nx, ny])  # 그림의 다음부분 탐색을 위해 큐에 추가


T = int(input().rstrip())

for _ in range(T):
    m, n, k = map(int, input().rstrip().split())
    matrix = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        matrix[y][x] = 1

    answer = 0
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 1:   # 노드가 1이면 그림 시작
                answer += 1
                bfs(x, y)

    print(answer)
