import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = 0

# 1. 정사각형이면 왼쪽,왼쪽 위,위 비교하기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1],dp[i-1][j]) + 1

# 2. dp테이블에서 가장 큰 값 구하기
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans**2) 
