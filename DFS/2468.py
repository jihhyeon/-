# 어떤 지역의 높이 정보 = N
# 안전한 영역 : 물에 잠기지 않는 지점들이 상하좌우에 있으며 크기가 최대인 영역
# 안전영역의 최대 개수를 계산하는 프로그램
# NxN
# 비 높이 이하인 영역 = 0, 방문처리 = 1, 비 높이 이상인 영역 = 2
# 상하좌우 다니면서 0 아닌 것들 개수 구하기
from collections import deque
import sys
sys.setrecursionlimit(10000000)
n = int(input())
graph = []
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#높이 h 이상인 것만 살아남을 수 있음
def dfs(x, y, h):
    #방문처리
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>h and visited[nx][ny]==0:
            dfs(nx, ny, h)


for h in range(101):
    _cnt = 0
    visited = [[0]*n for _ in range(n)]#방문전
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and visited[i][j] == 0:
                dfs(i,j,h)
                _cnt += 1
    cnt = max(cnt, _cnt)
print(cnt)



            
            
            



