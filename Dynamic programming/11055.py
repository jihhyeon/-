"방법 1"
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# i까지 증가하는 부분 수열의 합
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        # 이전 수가 더 크다면 자기자신(arr), dp의 값을 현재 dp로 지정해줘야함
        else:
            dp[i] = max(dp[i], arr[i])
print(max(dp))

"방법2"
import sys
input = sys.stdin.readline

a = int(input())
data = list(map(int, input().split()))
dp = [i for i in data] # dp에 원래 값들 넣기

for i in range(a) :
	for j in range(i) :
		if data[j] < data[i] :
			dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))