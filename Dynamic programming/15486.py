import sys
input = sys.stdin.readline

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
dp = [0 for _ in range(n + 1)] # i일차에 얻을 수 있는 최대 이익

for i in range(1, n + 1):
    # dp 갱신 1 (이전까지의 최댓값)
    dp[i] = max(dp[i], dp[i - 1])
    print(i)
    fin_date = i + t[i] -1 # 당일 포함으로 -1해주기
    print('당일포함 끝나는 날', fin_date)
    if fin_date <= n:# 최종일 이전에 일이 끝나는 경우
        # dp 갱신 2 (끝나는 날 값 갱신해주기)
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구함
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
        print(dp)

print(max(dp))

