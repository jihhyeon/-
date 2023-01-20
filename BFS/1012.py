from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()#큐 만들기
    queue.append((a,b))
    graph[a][b] = 0#방문처리

    while queue:
        x, y = queue.popleft()#가장 왼쪽 요소 반환 및 삭제
        for i in range(4):
            nx = x+dx[i]#0,0,1,-1
            ny = y+dy[i]#1,-1,0,0
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))#오른쪽 끝에 삽입
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]#초기 0으로 설정
    
    #k 위치에 1 할당
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):#행
        for b in range(m):#열
            if graph[a][b] == 1:#배추 심어진 곳에 bfs진행
                bfs(graph, a, b)
                cnt += 1
    print(cnt)