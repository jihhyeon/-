from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
print(graph)
cnt = 0
area = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    new = 0
 
    while queue:
        x, y = queue.popleft()
        print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                new += 1
                queue.append([[nx,ny]])
    return new
                
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            area.append(bfs(graph,i,j))#넓이 저장
            cnt += 1#개수저장

print(max(area), cnt)