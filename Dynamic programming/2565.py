"""n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x:x[1])
ans = []
print(array)

for i in range(n):#기준이 돌아가게끔
    print(i)
    a = array[i]#[4,1]
    cnt = 1
    for j in range(n):
        print(array[j][0], array[j][1], a[0], a[1])
        if array[j][0] < a[0] and array[j][1] < a[1]:
            print(array[j][0],'<', a[0], '/',array[j][1], '<', a[1])
            cnt += 1
        elif array[j][0] > a[0] and array[j][1] > a[1]:
            print(array[j][0],'<', a[0], '/',array[j][1], '<', a[1])
            cnt += 1
    if cnt > 1:
        ans.append(n - cnt)
    print(ans)

print(min(ans))"""
n = int(input())
w = []
w_b = []
dp = [0 for i in range(n)]
for i in range(n):
    w.append(list(map(int, input().split())))
w.sort(key = lambda x:x[0])#a전봇대 기준으로 정렬

for i in range(n):
    w_b.append(w[i][1])

#b전봇대에서 가장 긴 증가하는 부분수열 구하기
for i in range(n):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))