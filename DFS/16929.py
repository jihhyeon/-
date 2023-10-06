import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0]*m for _ in range(n)]
result = []

def dfs(x,y,prex,prey,cnt):
    if visited[x][y] and cnt >= 4:
        result.append('yes')
        return
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[x][y]:
            if nx != prex and ny != prey:
                dfs(x,y,prex,prey,cnt + 1)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,i,j,0)
if result:
    print('YES')
else:
    print('NO')