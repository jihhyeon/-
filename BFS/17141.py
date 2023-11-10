from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

def bfs(v):
    que = deque(v)
    # count해야하기 때문에 -1로 설정하기 !!!
    visited = [[-1]*n for _ in range(n)]
    m = 0 # 최소 횟수를 찾기 위한 변수

    # 바이러스들은 방문처리 해주기
    for x, y in que:
        visited[x][y] = 0
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않고, 벽이 아닌 곳
                if visited[nx][ny] == -1 and lab[nx][ny] != 1:
                    que.append([nx,ny])
                    visited[nx][ny] = visited[a][b] + 1
                    m = max(m, visited[nx][ny])# 최소 횟수로 갱신해주기
                    # print(*visited, sep = '\n')
    # bfs가 끝난 이후 바이러스에 감염되지 않은 빈칸이 있다면 inf 리턴
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and lab[i][j] != 1:
                return float('inf')
    return m

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
virus = []
answer = float("inf") # 최솟값을 찾기 위해 초깃값을 inf로 설정

for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i,j])
            
vir = list(combinations(virus, m))

for v in vir:
    answer = min(bfs(v), answer)

if answer == float('inf'):
    print(-1)
else:
    print(answer)

