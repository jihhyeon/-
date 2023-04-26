n = int(input())
array = list(map(int, input().split()))
ans = [0]*n

for i in range(1, n+1):#키는 1부터 시작
    t = array[i-1]
    cnt = 0
    print(cnt)
    for j in range(n):
        if cnt == t and ans[i] == 0:
            print(j, ans[j], cnt)
            ans[j] = i
            break
        elif ans[i] == 0:
            cnt += 1
