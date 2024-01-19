import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
warm_list = []

# dfs
def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny)

for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    warm = 0
    # 그래프에서 배추 찾기
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                warm += 1
    warm_list.append(warm)

    # 흰지렁이 마리수 출력

for i in range(len(warm_list)):
    print(warm_list[i])
