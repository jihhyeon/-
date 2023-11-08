from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0]*n for _ in range(n)]

# 1. 섬을 찾자
def find_island(x,y):
    global count_island
    que = deque()
    que.append([x,y])
    while que:
        map[x][y] = count_island
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and map[nx][ny] == 1:
                visited[nx][ny] = 1
                map[nx][ny] = count_island
                que.append([nx, ny]) 
    count_island += 1
    
count_island = 1
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and visited[i][j] == 0:
            find_island(i, j)
            print(map)
            print(count_island)

# 2. 섬과 섬 연결하기
def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
    q = deque()

    for i in range(n):
        for j in range(n):
            if map[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0
    print(z)

    while q:
        x, y = q.popleft()
        print('xy', x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
                if map[nx][ny] > 0 and map[nx][ny] != z:
                    answer = min(answer, dist[x][y])
                    return
                # 바다를 만나면 dist를 1씩 늘린다.
                if map[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    print(nx, ny)
                    print(dist)
                    q.append([nx, ny])
answer = sys.maxsize
# for i in range(1, count_island):
#     bfs2(i)
bfs2(1)
print(answer)

