#공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날수 있음
#여행을 떠날 수 잇는 그룹 수의 최댓값
#공포도 최댓값 = a을 구하고 , a명의 팀 만들기 -> 최댓값 제외한 나머지 공포도는 낮은 순으로
#남은 공포도들도 위와 같은 방법으로 반복하기
import time
n = int(input())
scare = list(map(int, input().split()))
start_time = time.time()
# scare.sort(reverse = True)#내림차순 정렬, [3,2,2,2,1]
# answer = 0

# while True:
#     if len(scare) == 0:#scare 리스트에 원소 없을 시 break
#         break
#     print(scare)
#     for _ in range(scare[0]-1):
#         scare.pop()
#     scare.pop(0)#최댓값 삭제하기
#     answer += 1#그룹 더해주기
# end_time = time.time()
# print('final:', answer)
# print('time:', end_time - start_time)#시간 = 7.128715515136719e-05


#---------------------------
#공포도가 낮은 모험가부터 그룹을 결성하면 최대한 많은 그룹을 결성할 수 있음
#즉, 내림차순 정렬이 아닌 오름차순 정렬로 진행해야함
scare.sort()[1,2,2,2,3]

result = 0#총 그룹의 수
count = 0#현재 그룹에 포함된 모험가의 수

for i in scare:
    count += 1
    if count >= i:#현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        result += 1# 총 그룹의 수 증가시키기
        count = 0#초기화
print(result)

