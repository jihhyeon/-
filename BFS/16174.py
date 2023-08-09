import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [0,1]
dy = [1,0]
visited = [[0]*n for _ in range(n)]
que = deque()
que.append([0,0])

while que:
    x,y = que.popleft()
    if graph[x][y] == -1:
        print("HaruHaru")
        exit(0)
    start = graph[x][y]
    for i in range(2):
        nx = x + dx[i]*start
        ny = y + dy[i]*start
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            que.append([nx,ny])

print("Hing")