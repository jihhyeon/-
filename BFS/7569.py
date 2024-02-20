from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])

dx = [-1,1,0,0,0,0] # 상,하,좌,우,위(3차원), 아래(3차원)
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
ans = 0

def bfs():
    while que:
        a,b,c = que.popleft()
        for i in range(6):
            nx = b + dx[i]
            ny = c + dy[i]
            nz = a + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if box[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = 1
                    # 현재 값 = 이전값 + 1
                    box[nz][nx][ny] = box[a][b][c] + 1
                    que.append([nz,nx,ny])

que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1 and visited[i][j][k] == 0:
                que.append([i,j,k])
                visited[i][j][k] = True

bfs()

# 모든 상자가 1인지 확인, 맞으면 day 출력 아니면 -1 출력
all_one = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            ans = max(ans, box[i][j][k])

print(ans - 1)