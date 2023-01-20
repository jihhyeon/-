n = int(input())#줄선 사람들
pe = list(map(int, input().split()))#걸리는 시간

#시간 작은 순서로 정렬
pe.sort()
tot = []
cnt = 0
print(pe)
for i in range(n):
  #i번째 사람이 걸리는 시간
  a = pe[i]#1, 2, 3
  cnt += a#1, 3, 6
  print(cnt)
  tot.append(int(cnt))#[1,3,6]
  print('a: ', a)
  print('tot:', tot)
print(sum(tot))

# print(sum)