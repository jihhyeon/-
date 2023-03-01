n = int(input())
data_list = []

for _ in range(n):
    li = list(map(str, input().split()))
    data_list.append(li)
#key를 이용하여 점수를 기준으로 정렬
data_list.sort(key = lambda x:x[1])
print(data_list)

for i in range(n):
    print(data_list[i][0], end = ' ')