# dp + dfs 문제!!
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]# dp 테이블
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0

def dfs(x, y):
    if check[x][y]: # 방문한 적이 있다면 해당값을 그대로 가져와 사용
        return check[x][y]
    
    check[x][y] = 1 # 첫 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if forest[x][y] < forest[nx][ny]: # 이동할 곳에 대나무가 더 많다면
                check[x][y] = max(check[x][y], dfs(nx,ny) + 1)
    return check[x][y]

for i in range(n):
    for j in range(n):
        if not check[i][j]:
            dfs(i,j)
 
MAX = 0
for i in range(n):
    MAX = max(MAX, max(check[i]))
print(MAX)

"""
def dfs(size, x, y):
    global forest, max_move
    around = [] # 상하좌우 숲의 크기
    around_idx = []
    max_move += 1
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if size <= forest[nx][ny]:
                around.append(forest[nx][ny])
                around_idx.append([forest[nx][ny], nx, ny])
    # print(around)
    if around:
        min_value = min(around)
        for i in range(len(around_idx)):
            if around_idx[i][0] == min_value:
                # print('dfs', around_idx[i][0])
                dfs(around_idx[i][0],around_idx[i][1],around_idx[i][2])


for i in range(n):
    for j in range(n):
        visited = [[0] * n for _ in range(n)]
        max_move = 0
        # print('start', forest[i][j])
        dfs(forest[i][j],i,j) # 숲의 크기, 좌표
        # print('대나무숲 크기', max_move)
        ans = max(max_move, ans)

print(ans)"""
