n, m = map(int,input().split())
trees = list(map(int, input().split()))
start, end = 1, sum(trees)

while start <= end:
    mid = (start+end)//2

    #벌목된 나무 총합
    log = 0
    for i in trees:
        if i >=mid:
            log += i-mid
    print('log: ', log)

    if log >= m:
        start = mid+1
    else:
        end = mid-1
print(end)