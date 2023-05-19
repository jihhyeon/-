import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

que = deque()

def bfs():
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                que.append([nx, ny])

#익은 토마토 que에 넣어주기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])

bfs()

print(graph)
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)#코드 강제종료
    res = max(res, max(i))#열마다 돌면서 최대값 찾아주기
#처음 시작을 1로 했으니 1을 빼주기
print(res - 1)