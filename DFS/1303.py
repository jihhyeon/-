import sys
sys.setrecursionlimit(10*6)

n, m = map(int, input().split())
array = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(m)]
w,b = 0,0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y,team):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and array[nx][ny] == team:
            cnt += 1
            dfs(nx, ny, team)
    return cnt

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt = 1
            if array[i][j] == 'W':
                w += dfs(i,j,'W')**2
            else:
                b += dfs(i,j,'B')**2
print(w,b)