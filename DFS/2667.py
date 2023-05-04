import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
visited = [[0]*n for _ in range(n)]
cnt = 0#단지수
ans = []#집의 수
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    global count
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                dfs(nx,ny)
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = 1
            cnt += 1
            ans.append(dfs(i, j))
ans.sort()
print(cnt)
for i in ans:
    print(i)


