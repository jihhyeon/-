#bfs
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())#블록수
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = []
count = 0#총 블록수

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    visited[x][y] = 1#방문처리
    que = deque()
    que.append([x,y])
    cnt = 1
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append([nx,ny])
    
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs(i,j))
            count += 1
result.sort()
print(count)
for i in result:
    print(i)