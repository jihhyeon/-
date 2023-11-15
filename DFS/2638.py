# 외부공기를 체크해주는 것이 포인트!!
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
time = 0

# 외부공기는 2로 변환시키기
def air(x,y, visited):
    graph[x][y] = 2
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
                visited[nx][ny] = True
                graph[nx][ny] = 2
                air(nx,ny,visited)

# 맞닿은 개수 체크하기
def check(x,y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 2:
            cnt += 1
    return cnt

while True:
    time += 1
    ch_list = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    air(0,0,visited)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and check(i,j) > 1:
                ch_list.append([i,j])

    # 맞닿은 부분 외부공기로 전환해주기           
    for i in ch_list:
        graph[i[0]][i[1]] = 2

    notagain = True

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                notagain = False
    
    if notagain:
        break

print(time)
    



                

