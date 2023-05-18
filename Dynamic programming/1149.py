n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

#이전의 값들 중 같은 색을 제외한 min값 더해주기
for i in range(1,n):
    array[i][0] = min(array[i-1][1], array[i-1][2]) + array[i][0]
    array[i][1] = min(array[i-1][0], array[i-1][2]) + array[i][1]
    array[i][2] = min(array[i-1][0], array[i-1][1]) + array[i][2]
print(min(array[n-1]))