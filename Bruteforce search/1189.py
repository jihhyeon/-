import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

r,c,k = map(int, input().split())
array = [list(map(str, input().rstrip())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
answer = 0
total = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x, y, cnt):
    global answer
    visited[x][y] = 1
    if x == 0 and y == c-1:
        if cnt == k:
            answer += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0 and array[nx][ny] != 'T':
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0#다시 0으로 해줘야하마

dfs(r-1, 0, 1)
print(answer)


