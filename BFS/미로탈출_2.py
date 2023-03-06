#괴물 : 0, 괴물 x : 1
#탈출을 위해 움직여야하는 최소 칸의 개수 -> 괴물 없는 부분으로 다녀야함
#이유 : 1로 깊게 다니다가 0이 있으면 다시 1로 돌아가야하므로 , 1의 인접지역을 확인하는 bfs방법으로 풀기
#노드 수를 더해감
from collections import deque

def bfs(graph, x, y, visited, check):
    visited[x][y] = 1
    check[x][y] = 1#이동 기록도 1부터 시작임!
    que = deque()
    que.append([x, y])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    que.append([nx, ny])
                    visited[nx][ny] = 1
                    check[nx][ny] = check[a][b]+1
                    # print(check[nx][ny])
            
    return check[n-1][m-1]#맨마지막칸 출력

n, m = map(int, input().split())#n = 행, m = 열
visited = [[0]*m for _ in range(n)]#방문기록
check = [[0]*m for _ in range(n)]#횟수 더하기
graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int, input())))

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             print(bfs(graph, i, j, visited))
print(bfs(graph, 0,0,visited, check))
