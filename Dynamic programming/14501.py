"""1. 인덱스 0부터 돌아가며 순차적으로 탐색하기
2. 끝나는 날이 인덱스7이상이면 넣지 말고 멈추기
3. 이익들 리스트에 저장한 후 max값 뽑기
"""
import sys
input = sys.stdin.readline
n = int(input())
t, p = [], []
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

#dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
dp = [0] * (n+1)
max_value = 0

for i in range(n-1, -1,-1):
    time = t[i] + i
    print(i, time)
    #상담이 기간안에 끝나는 경우
    if time <= n:
        print('if',time)
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
        print(max_value)
    else:
        dp[i] = max_value
print(max_value)



    