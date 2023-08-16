n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
d = [0]*n

d[0] = arr[0]

if n > 1:
    d[1] = arr[0] + arr[1]

if n > 2:
    d[2] = max(arr[2] + arr[1], arr[2] + arr[0], d[1])#지금-전, 지금-전전, 

for i in range(3, n):
    #현재 포도주를 마시지 않음, 현재포도주마심-전전마심-이전 마시지않음, 현재마심-이전마시지않음
    d[i] = max(d[i-1], d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i])
    print(d[n-1])