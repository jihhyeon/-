import time
def solution(N, stages):
    answer = []
    real_answer = []
    stages.sort()#오름차순 정렬[1,2,2,2,3,3,4,6]
    in_people = len(stages)#8
    for i in range(1, N+1):
        not_clear = stages.count(i)#멈춘 사람들 초기화

        if in_people == 0:
            fail = 0
        else:
            fail = not_clear / in_people
        answer.append([i, fail])
        in_people -= not_clear
    
    answer.sort(key = lambda x: (-x[1], x[0]))
    for i in range(len(answer)):
        real_answer.append(answer[i][0])

        
                
        
    return real_answer