n, m = map(int,input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2

    #벌목된 나무 총합
    log = 0
    for i in trees:
        if i >=mid:
            log += i-mid
        if log > m:#시간초과 해결, 절단된 나무를 추가하는 중 이미 m을 넘어버린 경우 중단
            break

    if log >= m:#벌목된 나무 총합이 중간보다 크면
        start = mid+1
        #위로가서 바뀐 start값으로 mid 재설정

    else:#벌목된 나무 총합이 중간보다 작으면
        end = mid-1
        #위로가서 바뀐 end값으로 mid 재설정
print(end)#높이의 최대값이기 때문에 end 출력