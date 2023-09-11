# BFS방법
"""import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    o = 0
    v = 0

    while q:
        x, y = q.popleft()

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    continue
                elif graph[nx][ny] == 'v':
                    v += 1
                elif graph[nx][ny] == 'o':
                    o += 1
                q.append((nx, ny))
                visited[nx][ny] = 1

    return o, v



n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(input().rstrip()))

# 나 자신 또한 늑대인지 양인지 땅인지 구분해야하기 때문에 (0,0)포함
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

sheep, wolf = 0, 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)"""

# DFS 방법
import sys
sys.setrecursionlimit(10 ** 6)
r, c = map(int, input().split())
yard = [list(map(str, input().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sheep = 0
wolf = 0
a,b=0,0

def dfs(x,y):
    global s, w
    # 나 자신 먼저 검증하고
    if 0 <= x < r and 0 <= y < c:
        if yard[x][y] != '#' and visited[x][y] == 0:
            visited[x][y] = True
            if yard[x][y] == 'o':
                s += 1
            if yard[x][y] == 'v':
                w += 1
            # 상하좌우 검증하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx,ny)
            # 조건 만족해 dfs 돌면 True
            return True
        # 조건 만족 못하면 False
        return False

for i in range(r):
    for j in range(c):
        s, w = 0, 0
        if visited[i][j] == 0 and yard[i][j] != '#':
            if dfs(i,j) == True:
                if s > w:
                    sheep += s
                else:
                    wolf += w
print(sheep, wolf)
