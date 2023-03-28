#bfs 상하좌우 차이범위에 해당하면 넣어주기
from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
result = 0

def bfs(x,y,index):
    #(x,y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append([x,y])
    que = deque()
    que.append([x,y])
    #현재 연합의 번호 할당
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(graph[a][b] - graph[nx][ny]) <= r:
                    print(graph[a][b], graph[nx][ny])
                    union[nx][ny] = index
                    que.append([nx,ny])
                    summary += graph[nx][ny]
                    count += 1
                    united.append([nx,ny])
    for i, j in united:
        graph[i][j] = summary//count
    print(count, index, union, united, summary)
    return count

total_count = 0

#더 이상 인구이동을 할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1

print(total_count)