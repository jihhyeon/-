import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# i까지의 가장 긴 감소하는 부분 수열의 길이
dp = [1 for _ in range(n)] # 혼자만 가능할 때는 길이가 1이므로


for i in range(1, n):# dp인덱스 1부터 시작 (0은 앞의 값이 없으니까)
    for j in range(i):# i의 앞부분 탐색
        if arr[i] < arr[j]:# 앞부분이 더 크면
            dp[i] = max(dp[i], dp[j] + 1) # 현재 dp값과 이전 dp값 + 1의 값 중 max값으로 갱신
            print(i,j)
            print(arr[i],'<' , arr[j])
            print(dp)