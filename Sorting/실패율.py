import time
def solution(N, stages):
    answer = []
    real_answer = []
    st_time = time.time()
    stages.sort()#오름차순 정렬[1,2,2,2,3,3,4,6]
    in_people = len(stages)#8
    for i in range(1, N+1):
        not_clear = 0#멈춘 사람들 초기화
        for j in stages:
            if i == j:#해당 stage를 못깬 사람들
                not_clear += 1#1
            else:
                not_clear += 0
        answer.append([i, not_clear/in_people])
        in_people -= not_clear
        
    answer.sort(key = lambda x: (-x[1], x[0]))
    for i in range(len(answer)):
        real_answer.append(answer[i][0])
    end_time = time.time()
    print('time:', end_time - st_time)
        
                
        
    return real_answer