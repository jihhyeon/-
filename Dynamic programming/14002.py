n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
save_list = []

# 1. 수열의 길이
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))

# 2. 수열 구하기
max_dp = max(dp)
for i in range(n - 1, -1,-1):
    if dp[i] == max_dp:
        save_list.append(arr[i])
        max_dp -= 1

save_list.sort(reverse = False)
print(*save_list)

