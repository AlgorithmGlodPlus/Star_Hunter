import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and maze[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

bfs()
print(visited[N-1][M-1])