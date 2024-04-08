import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())

wall = [[0]*(w+2) for _ in range(h+2)]

for i in range(1, h+1): # 위, 아래, 왼쪽, 오른쪽을 0으로 채워줌
    wall[i][1:w+1]=map(int, sys.stdin.readline().split())

dx = [-1,-1,0,0,1,1]
dy=[[0,1,-1,1,0,1],[-1,0,-1,1,-1,0]] # 홀수 , 짝수

res = 0
queue = deque([])
visited = [[False] * (w + 2) for _ in range(h + 2)]
queue.append((0, 0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        if x % 2 == 1:
            ny = y + dy[0][i]
        else:
            ny = y + dy[1][i]

        if 0<=nx<h+2 and 0<=ny<w+2:
            if wall[nx][ny]==0 and not visited[nx][ny]: # 만약 0이고 아직 방문하지 않았다면
                visited[nx][ny]=True
                queue.append((nx, ny))
            elif wall[nx][ny]==1: # 만약 1이라면
                res+=1 # 결과 더해주기
print(res)