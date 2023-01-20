n, m = map(int,input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
print(start, end)

while start <= end:
    mid = (start+end)//2
    print('mid: ', mid)

    #벌목된 나무 총합
    log = 0
    for i in trees:
        if i >=mid:
            log += i-mid
    print('log: ', log)

    if log >= m:#벌목된 나무 총합이 중간보다 크면
        start = mid+1
        #위로가서 바뀐 start값으로 mid 재설정

    else:#벌목된 나무 총합이 중간보다 작으면
        end = mid-1
        #위로가서 바뀐 end값으로 mid 재설정
print(end)#높이의 최대값이기 때문에 end 출력