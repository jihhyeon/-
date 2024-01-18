import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
second = 0

q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], i,  j, 0)) # 바이러스 정보, 행, 열, 시간
q.sort() # 오름차순 정렬
print(q)
q = deque(q)

# 2. while문 
while q:
    vir, row, col, time = q.popleft()
    if time == s:
        break
# 3. 바이러스 종류마다 증식시키기 (for문 바이러스 종류 -> bfs 진행)
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = vir
            q.append((vir, nx, ny, time + 1))

# 4. 정답 출력
print(graph[x-1][y-1])
