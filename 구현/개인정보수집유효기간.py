"""
# 년과 월 => 일수로 변환하기(한달은 28일)
def time_convert(t):
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []
    
    #약관도 일수로 변환해주기
    for term in terms:
        name, period = term.split()
        term_dict[name] = int(period) *28
        
    for idx, privacy in enumerate(privacies):
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today : 
            answer.append(idx + 1)
    return answer
        
    """
def time_convert(t):
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dic = dict()
    today = time_convert(today) # 일 수로 변환하기
    answer = []
    
    for te in terms:
        kind, period = te.split()
        term_dic[kind] = int(period) * 28
    
    for i, pri in enumerate(privacies):
        period, kind = pri.split()
        convert_day = time_convert(period) + term_dic[kind]
        if convert_day <= today:
            answer.append(i+1)
    return answer
        
    
    
    
    
    
    
    
    
    
    