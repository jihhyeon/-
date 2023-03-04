"""서로 무게가 다른 볼링공을 고르려함
볼링공을 고르는 경우의 수를 구해라"""
n, m = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0
for i in range(len(weight)):
    for j in range(i+1, len(weight)):
        if weight[i] != weight[j]:
            cnt += 1
            print(weight[i], weight[j], cnt)
print(cnt)
#-------------------------------------
#a가 무게가 낮은 볼링공부터 높은 볼링공까지 순서대로 하나씩 확인 할 때
#b가 선택하는 경우의 개수 구해보기(무게는 a무게보다 커야함)
n, m = map(int, input().split())
weight = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in weight:
    array[x] += 1
    
result = 0

#1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n
print(result)

