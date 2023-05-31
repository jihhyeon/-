"""import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0#빙산 최소 년수
count = 0#빙산 덩어리 개수

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def reduce_length(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            graph[nx][ny] -= 1
            if graph[nx][ny] < 0:
                graph[nx][ny] == 0

def bfs(x,y):
    que = deque()
    visited[x][y] = 1
    que.append([x,y])
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append([nx, ny])


while True:
    visited = [[0]*m for _ in range(n)]
    #빙하 높이 줄이기
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                reduce_length(i, j)
    year += 1

    #줄어든 높이로 빙산개수 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                bfs(i,j)
                count += 1
    if count >= 2:
        print(year)
        break

"""
from collections import deque
import sys
input = sys.stdin.readline

d = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(y,x):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]

            if (0<=dr<n) and (0<=dc<m):
                if graph[dr][dc] == 0:
                    visited[r][c] += 1

                if not visited[dr][dc] and graph[dr][dc] != 0 :
                    queue.append([dr,dc])
                    visited[dr][dc] = True


n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


#두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램
time = 0
while True:
    count = 0#빙산의 개수
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if not visited[i][k] and graph[i][k]!=0:
                bfs(i,k)
                count +=1

    #빙산 녹이기
    for i in range(n):
        for k in range(m):
            if visited[i][k] :
                graph[i][k] -= (visited[i][k]-1)
                if graph[i][k] < 0: graph[i][k] = 0

    time += 1
    if count == 0:
        print(0)
        exit()
    if count >=2 :
        break

print(time-1)