import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# visited[x][y][0] = 벽 파괴 가능, visited[x][y][1] = 벽파괴 불가능
visited = [[[0] * 2 for _ in range(m)]for _ in range(n)]
visited[0][0][0] = 1
dx, dy = [-1,1,0,0], [0,0,-1,1]
ans = 0

def bfs(x,y,z):
    que = deque()
    que.append([x,y,z])

    while que:
        a,b,c = que.popleft()
        if a == n-1 and b == m-1 :
            return visited[a][b][c]
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이고, 벽파괴 기회를 사용하지 않은 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    que.append([nx,ny,1])
                
                # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    que.append([nx, ny, c])

    return -1

print(bfs(0,0,0))