from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    que = deque()
    que.append([0,0])
    # 검은 방을 흰 방으로 바꾼 횟수
    visited = [[-1]*n for _ in range(n)]
    visited[0][0] = 0
    while que:
        x, y = que.popleft()
        if x == n-1 and y == n-1 :
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    # 맨 왼쪽에 추가해서 흰방 먼저 탐색하게 함
                    que.appendleft([nx,ny])
                    # 흰방이면 이전 visited값으로 초기화
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny] == 0:
                    que.append([nx,ny])
                    # 검은 방이면 이전 visited에서 1 더해서 초기화
                    visited[nx][ny] = visited[x][y] + 1
                # print(visited)

print(bfs())
