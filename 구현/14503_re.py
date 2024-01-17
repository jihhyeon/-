import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]
visited[r][c] = 1
cnt = 1


while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4
        nr = r + dx[d]
        nc = c + dy[d]

        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r, c = nr, nc
                flag = 1
                break
    # 네 방향 모두 청소할 수 없을 때
    if flag == 0:
        if graph[r-dx[d]][c-dy[d]] == 1: # 후진했는데 벽일 경우
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d] 



