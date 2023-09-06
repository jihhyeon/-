n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

#10원이 되게하는 방법
#dp[1] : 1원이 되는 방법, dp[3] : 3원이 되는 방법
dp = [0] * (k+1)
dp[0] = 1
for c in coins:
    print(c)
    #1~10(1원), 2~10(2원), 5~10(5원))
    for i in range(c, k+1):
        dp[i] += dp[i-c]
        print(i,i-c, dp)
print(dp[k])