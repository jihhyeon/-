#3이 하나라도 포함되는 모든 경우의 수 출력하기 -> 1씩 증가시키며 확인하기
#경우의 수 : 24*60*60 = 86400전체 데이터가 100만개 이하일 떄는 완전탐색 가능
#시, 분, 초
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)