def solution(plans):
    finish = []
    stop = []
    # 1. 시간 -> 분단위로 변환하기
    for plan in plans:
        hour, minute = map(int, plan[1].split(':'))
        plan[1] = hour * 60 + minute
        plan[2] = int(plan[2])
    plans.sort(key = lambda x: x[1])
    
    def compare(whiletime):
        while stop:
                if whiletime == 0:
                    break
                sub, time = stop.pop(-1) # 과목, 남은 시간
                # 남은 시간이 더 많을 때
                if whiletime < time:
                    time -= whiletime # 90 - 30 
                    whiletime = 0 
                    stop.append([sub, time]) # 다시 넣어주기
                else:
                    if whiletime == time:
                        whiletime = 0
                        # 남은시간이 적을 때
                    else:
                        whiletime -= time
                    finish.append(sub)
                    
    # 2. plans돌면서 다음 playtime과 비교
    for i in range(len(plans)-1):
        dif = plans[i+1][1] - plans[i][1] # 다음 playtime과 시간차
        # 과제를 끝낼 수 있으면
        if dif == plans[i][2]:
            finish.append(plans[i][0])
        # 과제를 끝낼 수 없으면, stop에 추가하기
        if dif < plans[i][2]:
            stop.append([plans[i][0], plans[i][2] - dif])
        # 과제를 끝내고 시간이 남는다면
        if dif > plans[i][2]:
            finish.append(plans[i][0])
            whiletime = abs(plans[i][2] - dif) # 과제 가능한 시간
            # if stop:
            compare(whiletime)
    finish.append(plans[len(plans)-1][0])
    while stop:
        s,t = stop.pop(-1)
        finish.append(s)
    
    return finish