n = int(input())
array = list(map(int, input().split()))
dp1 = [1]*n
dp2 = [1]*n
for i in range(1, n):
    if array[i-1] >= array[i]:#전 >= 후
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if array[i-1] <= array[i]:#전 <= 후
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(dp1)
print(dp2)
print(max(max(dp1), max(dp2)))
