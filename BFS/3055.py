from collections import deque


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

sx, sy = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            sx, sy = i, j
            graph[i][j] = "."


def flood():
    water = []#함수 실행될때마다 설정
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*" and not visited[i][j]:
                water.append((i, j))
                visited[i][j] = True

    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while q:
        cnt += 1
        #물 확장
        flood()
        #고슴도치 이동
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if graph[nx][ny] == ".":
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == "D":
                        return cnt

    return "KAKTUS"


print(bfs(sx, sy))