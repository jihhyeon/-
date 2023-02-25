"""구명보트는 한번에 최대 2명씩 + 무게제한 o
구명보트를 최대한 적게 사용해 모든 사람 구출하려고함
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 return
1. 내림차순 정렬하기 -> [80,70,50,50]
2. 가장 적은 횟수로 사람 이동 => 제일 무거운사람+제일 가벼운사람 묶어서 처리하기
"""
from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people, reverse = True)
    que = deque(people)
    
    while len(que)>1:
        if que[0] + que[-1] <= limit:
            answer += 1
            que.popleft()#최대 빼내고
            que.pop()#최소 빼내기
        else:
            answer += 1
            que.popleft()
    if que:
        answer += 1
        
    return answer