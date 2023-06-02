#최장 길이 부분 수열 문제
n = int(input())
num = [0]
for i in range(n):
    num.append(int(input()))
dp = [1]*(n+1) #i번째까지 증가했을 때 수열의 최대 길이
print(num, dp)

#i = 현재값, j = 이전값들(0~i-1)
for i in range(1,n+1):
    for j in range(1,i):
        print(i, j)
        if num[j]<num[i]:#현재값보다 이전값이 작을 경우
            print(i,num[j], j, num[i])
            dp[i]=max(dp[i],dp[j]+1)
            print(dp)

print(n-max(dp))
#가장 긴 증가하는 부분 수열을 제외한 나머지가 이동하는 것이기 때문!