import sys
sys.setrecursionlimit(10*5)
input = sys.stdin.readline
n,m,k = map(int, input().split())
graph = [[0]*m for _  in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
visited = [[False]*m for _  in range(n)]
answer = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                cnt += 1#음식물 개수 더해주기
                dfs(nx,ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i,j)
            answer = max(cnt, answer)
print(answer)


    