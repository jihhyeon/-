from collections import deque
n, x = map(int, input().split())
num = list(map(int, input().split()))
# que = deque(num)
cnt = 0
start, end = 0, len(num)-1
while start <= end:
    mid = (start+end)//2
    print(start, end)
    print('mid', mid, 'cnt', cnt)
    if num[mid] == x:
        cnt += 1
        num.pop(mid)
    elif num[mid] < x:
        start = mid + 1
    else:
        end = mid -1

if cnt == 0:
    print(-1)
else:
    print(cnt)


