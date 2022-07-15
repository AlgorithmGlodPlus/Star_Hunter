import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
picture = [list(input().rstrip()) for _ in range(N)]

colors = ['R', 'G', 'B']
visited_1 = [[0] * N for _ in range(N)] # 색약 아닌 사람
visited_2 = [[0] * N for _ in range(N)] # 색약인 사람

area_1 = [0] * 3
area_2 = [0] * 3

def bfs(i, j, color, v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque()
    que.append([i, j])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and picture[nx][ny] == color and v[nx][ny] == 0:
                que.append([nx, ny])
                v[nx][ny] = 1

for i in range(N):
    for j in range(N):
        if visited_1[i][j] == 0:
            if picture[i][j] == colors[0]:
                bfs(i, j, colors[0], visited_1)
                area_1[0] += 1
            elif picture[i][j] == colors[1]:
                bfs(i, j, colors[1], visited_1)
                area_1[1] += 1
            else:
                bfs(i, j, colors[2], visited_1)
                area_1[2] += 1

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited_2[i][j] == 0:
            if picture[i][j] == colors[0]:
                bfs(i, j, colors[0], visited_2)
                area_2[0] += 1
            elif picture[i][j] == colors[2]:
                bfs(i, j, colors[2], visited_2)
                area_2[2] += 1

print(sum(area_1), sum(area_2))