#배열 A의 모든 원소 합이 최대가 되도록
#n = 배열의 원소 개수, k = 바꿔치기 연산 횟수
#a의 가장작은 원소와 b의 가장큰원소 바꾸기
#배열 a는 오름차순, 배열 b는 내림차순 => 인덱스 같게하기
#단,배열 a에서 가장 작은 원소가 배열 b에서 가장 큰 원소보다 작을 때만 교체 수행
import time
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
start_time = time.time()
# a.sort()#1,2,3,4,5
# b.sort(reverse = True)#6,6,5,5,5

# for i in range(k):
#     a[i] = b[i]

#a원소가 b원소보다 클 수도 있음 
for i in range(k):
    if a[i]<b[i]:#작은 경우만 바꿔주고
        a[i], b[i] = b[i], a[i]
    else:
        break
    
end_time = time.time()
print(a, sum(a))
print('time: ', end_time-start_time)

