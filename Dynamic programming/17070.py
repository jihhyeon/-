import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

#가로, 세로, 대각선
dp = [[[0,0,0] for _ in range(n)] for _ in range(n+1)]
dp[1][1] = [1,0,0]

for i in range(1, n+1):
    for j in range(1, n):
        if i == j == 1:
            continue
        if arr[i][j] == 0:
            # 가로
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            # 세로
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][2]
            # 대각선의 경우 위와 왼쪽이 비어있어야함
            if arr[i-1][j] == arr[i][j-1] == 0:
                dp[i][j][2] = sum(dp[i-1][j-1])
print(sum(dp[n][n-1]))
