def solution(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    pers = ['R','T','C','F','J','M','A','N']
    mbti = {x:0 for x in pers}#지표별 딕셔너리 만들기 : 초기갑=0
    
    for s,c in zip(survey,choices):#길이가 같아 zip가능
        if c < 4:
            mbti[s[0]] += score[c-1]
        else:
            mbti[s[1]] += score[c-1]
            
    for i in range(0,len(pers),2):
        if mbti[pers[i]] >= mbti[pers[i+1]]:#rt/cf/jm/an 고르기
            answer += pers[i]
        else:
            answer += pers[i+1]
        
    return answer