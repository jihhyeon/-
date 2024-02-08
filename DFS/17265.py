import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(str, input().split())) for _ in range(n)]
max_dp = [[-1e9 for _ in range(n)] for _ in range(n)]
min_dp = [[1e9 for _ in range(n)] for _ in range(n)]
max_dp[0][0] = int(grid[0][0])
min_dp[0][0] = int(grid[0][0])
dy, dx = [0, 1], [1, 0]

def operation(a, b, oper):
    if oper == '*':
        return a*b
    if oper == '+':
        return a+b
    if oper == '-':
        return a-b
def get_dp(y, x, oper):
    for i in range(2):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if grid[ny][nx].isdigit():
                max_dp[ny][nx] = max(max_dp[ny][nx], operation(max_dp[y][x], int(grid[ny][nx]), oper))
                min_dp[ny][nx] = min(min_dp[ny][nx], operation(min_dp[y][x], int(grid[ny][nx]), oper))
                get_dp(ny, nx, '')
            else:
                max_dp[ny][nx] = max_dp[y][x]
                min_dp[ny][nx] = min_dp[y][x]
                get_dp(ny, nx, grid[ny][nx])
get_dp(0, 0, '')
print(max_dp[n-1][n-1], min_dp[n-1][n-1])