#i-1, i-2만 보면 된다
n= int(input())#식량 창고 개수(3<=n<=100)
cnt = list(map(int, input().split()))#각 창고에 저장된 식량의 개수 k

#dp테이블 만들기
d = [0]*100
d[0] = cnt[0]
d[1] = max(cnt[0],cnt[1])

for i in range(2,n):
  d[i] = max(d[i-1], d[i-2]+cnt[i])
  print(i, d[i])

print(cnt[n-1])