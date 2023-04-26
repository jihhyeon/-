#민규가 카드 n개를 갖기 위해 지불해야하는 금액의 최댓값
"""n = int(input())
array = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    ans = [array[i]]
    if i == (n-1):
        dp[i] = array[i]
    else:
        ans.append(array[(n-1)-(i+1)]+array[i])
        if n % (i+1) == 0:
            ans.append(array[i]*(n//(i+1)))
        dp[i] = max(ans)
print(max(dp))"""
n = int(input())
d = [0] * (n+1)
p = [0] + list(map(int, input().split()))
print(p)
d[1] = p[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if d[i] < d[i-j] + p[j]:
            d[i] = d[i-j] + p[j]
print(d[n])