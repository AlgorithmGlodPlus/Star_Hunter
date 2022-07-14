#### 다시 풀어보기

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
maze = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

def bfs():
    answer = 'IMPOSSIBLE'

    dx = [1, -1, 0, 0]  # 행의 방향
    dy = [0, 0, 1, -1]  # 열의 방향
    que = deque()

    # 처음 지훈의 위치와 불의 위치 탐색
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                que.append([i, j, 1])
                visited[i][j] = 1
            elif maze[i][j] == 'F':
                que.append([i, j, -1])

    while que:
        x, y, time = que.popleft()

        # 미로 탈출
        if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and maze[x][y] != 'F' and time > 0:
            answer = time
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 네 방향의 x, y가 벽이 아닌 경우 탈출구 탐색
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#':
                # pop한 데이터가 지훈이일 경우
                if time > 0 and maze[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny, visited[nx][ny]])
                    maze[nx][ny] = 'J'
                # 불일 경우
                elif time == -1 and maze[nx][ny] != 'F':
                    que.append([nx, ny, -1])
                    maze[nx][ny] = 'F'

    return answer

print(bfs())