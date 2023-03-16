#n가지 종류의 화폐, 개수를 최소한으로 이용해 가치의 합이 m원이 되도록 
#불가능할 때는 -1 출력하기
#1. 15-3=12, 12-3=9, ...
#2. 4-3 = 1 1이 없으므로 -1
#여기서 dp 테이블 : 금액 i를 만들 수 있는 최소한의 화폐개수
#dp(i-k)를 만드는 방법이 존재하는 경우, k = 화폐단위 -> dp(i) = min(dp(i), dp(i-k)+1)
#                    존재하지 않는 경우 -> dp(i)=10001 (10001은 특정 금액을 만들 수 있는 화폐조합이 없다는 의미)

import sys

# 정수 N, M을 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())

# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
