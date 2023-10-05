# 출력 : 걸리는 시간, 녹기 한시간 전에 남아있는 치즈조각이 놓여있는 칸의 개수
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cheese = []
time = 0

def find_air():
    visited = [[False] * m for _ in range(n)]
    que = deque()
    que.append([0,0])
    cnt = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append([nx,ny])
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    cnt += 1
    cheese.append(cnt)
    return cnt


while True:
    cnt = find_air()
    if cnt == 0:
        break
    time += 1
print(time)
print(cheese[-2])


