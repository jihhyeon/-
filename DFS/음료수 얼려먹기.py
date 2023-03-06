#0인것을 끝까지 보고 개수를 세어야함 -> dfs
def dfs(graph, x, y, visited):
    visited[x][y] = 1#방문처리해주기
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            if graph[nx][ny] == 0:#구멍 뚫려있을 경우
                dfs(graph, nx, ny, visited)

n,m = map(int, input().split())#n = 행개수, m = 열개수
print(n, m)
graph = []#구멍 뚫려있는지 여부
visited = [[0]*m for _ in range(n)]#방문 여부
cnt = 0
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
print(visited)
for i in range(n):
    for j in range(m):
        if (visited[i][j] == 0) and (graph[i][j] == 0):
            dfs(graph, i, j, visited)
            cnt += 1
print(cnt)


    