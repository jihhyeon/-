#n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하기
#모든 동전의 합을 최대로 정하기
#target 이하의 값은 모두 만들 수 있음
#그리디 알고리즘인 이유: 작은 동전부터 하나씩 확인하며 target을 증가 시키고 가장 작은 target값을 찾아가기 때문
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 0
for i in coin:#1,1,2,3,9
    print(target+1)
    if target + 1 < i:
        break
    target += i#target+1이 i보다 큰 경우
    print(i,target)

print(target+1)#target + 1이 i 보다 작을 경우이기 때문


    