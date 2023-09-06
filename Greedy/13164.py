from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().rstrip())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = []

def bfs(x,y):
    global cnt
    visited[x][y] = 1
    que = deque()
    que.append([x,y])
    max_cnt = 0

    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <=ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 'L':
                    visited[nx][ny] = 1
                    visited_cnt[nx][ny] = visited_cnt[a][b] + 1
                    max_cnt = max(max_cnt,visited_cnt[nx][ny])
                    que.append([nx,ny])
    # print(visited_cnt)
    ans.append(max_cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            cnt = 0
            visited = [[0]*m for _ in range(n)]
            visited_cnt = [[0]*m for _ in range(n)]
            bfs(i,j)
print(max(ans))