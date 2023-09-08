import sys
from collections import deque
input = sys.stdin.readline
n, m, t = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*m for _ in range(m)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    gram = 10001
    visited[x][y] = 1
    que = deque((x,y))

    while que:
        a, b = que.popleft()

        #공주에게 도착하면 최소값 return 하기
        if a == n-1 and b == m-1:
            #gram만나지 않은 시간과 gram 만난 시간 중 최소값 구하기
            return min(visited[a][b]-1, gram)
        
        #그람을 만났을 때부터는 gram에 거리 저장!!이 부분이 핵심
        if graph[a][b] == 2:
            gram = visited[a][b] -1 + abs(n-1-a) + abs(m-1-b)
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

                #그람 만났을 때도 append 해주기
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    visited[nx][ny] += visited[a][b] + 1
                    print(nx,ny,visited)
                    que.append([nx,ny])

    return gram

res = bfs(0,0)
if res > t:
    print('Fail')
else:
    print(res)

                






    

