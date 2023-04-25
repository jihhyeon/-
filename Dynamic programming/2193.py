n = int(input())

dp = [0]*(n+1)
dp[1] = 1

#인덱스 = n, dp[n] = 각 자리의 이친수개수
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])



