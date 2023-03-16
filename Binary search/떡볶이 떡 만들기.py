n, m = map(int, input().split())
height = list(map(int, input().split()))#19, 15 10 17
start, end = 0, max(height)#0,,,,19
result = 0
print(n, m, height)


while start <= end:
    mid = (start + end) // 2
    #손님이 가져가는 길이
    rice = 0
    for i in height:
        if i > mid:
            rice += i - mid
    #손님이 가져가는 길이가 m보다 작을 경우 더 많이 자르기(끝점 감소)
    if rice < m:
        end = mid -1
    #손님이 가져가는 길이가 m보다 크거나 같은 경우 덜 자르기(시작점 증가)
    else:
        result = mid#최대한 덜 잘랐을 때가 정답이므로 result에 기록하기
        print(start, end, result)
        start = mid + 1
print(result)

