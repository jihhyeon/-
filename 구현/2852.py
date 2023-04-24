"""출력(이기고 있던 시간) = 48분 - 득점한 시간, 
ex 1) 1일때
1 = 48- 20 = 28분동안 이기고 있었음
ex 2) 1이상일때
1 = 현재 팀이 득점한 시간 - 다음팀이 득점한시간 = 20분(1:0) --- 이시간
2 = 현재 팀이 득점한 시간 - 다음팀이 득점한 시간 = 10분 20초(1:1)
2 = 현재 팀이 득점한 시간 - 48분 = 16분 30초(1:2) --- 이시간 출력하기
ex 3) 
1 = 1분 10초(1:0) , 48-1:10 = 46분 50초, 45:30 - 1:10 = 44:20
1 = 1:10(2:0), 46분50초 - 2분 20초 = 44분 30초, 44:20 + (46:40 - 45:30) = 45:30
2 = 43:10초(2:1), 
(2:2)가 될때 :
딕셔너리 or 리스트(1번 인덱스, 2번 인덱스에 저장하기)
1. 1->2로 바뀔때, 바뀌었는데 아직 1의 점수가 높을 때 => 계속해서 더해가기
2. 마지막 리스트에 48:00추가하기(빼줄수 있도록)
"""
import sys
input = sys.stdin.readline
n = int(input())
score = {1:0, 2:0}
time = {1:0, 2:0}
ans = {1:0, 2:0}
state = 0

for _ in range(n):
    team, t= input().split()
    team = int(team)
    mi, sec = map(int, t.split(':'))
    t = mi*60 + sec#초로 변환시켜주기 1:10 -> 70초
    score[team] += 1#팀에 해당하는 점수 올리기
    print(t)

    if state == 0:
        time[team] = t
        state = team

    elif state != 0 and score[1] == score[2]:
        ans[state] += t - time[state]
        state = 0

if state != 0:
    ans[state] += 60*48-time[state]

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))








