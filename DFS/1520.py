import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j] = (1,1) 좌표에서 (i,j)까지의 경로 개수
# 실제 경로가 0인 경우도 있을 수 있으니 -1로 설정
dp = [[-1] * m for _ in range(n)]
visited = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
end_n, end_m = 3,4

def dfs(x,y):
    print(x, y)
    if x == end_n and y == end_m:
        print('first')
        return 1

    # 이미 방문한 적이 있다며느 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        print('second')
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if map[nx][ny] < map[x][y]:
                print('mid')
                ways += dfs(nx, ny)
                print(ways)
    dp[x][y] = ways
    print(*dp, sep = '\n')
    return dp[x][y]

dfs(0,0)
# print(visited_dfs)



