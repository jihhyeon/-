"""1. 균형잡힌 문자열 u : (와)의 개수가 같아질 때 거기까지 반환, v : 나머지 + 없으면 빈칸""
2. 올바른 괄호 문자열 : 이미 균형잡힌 문자열에서 걸러졌기 때문에 앞이 "("이면 올바른 문자
재귀함수를 이용한 문제
"""
#균형잡힌 문자열
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
#올바른 괄호 문자열      
def check_proper(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False#쌍이 맞지 않는 경우 False 반환
            count -= 1
    return True#쌍이 맞는 경우 True 반환

def solution(p):
    answer = ''
    if p == "":
        return answer
    idx = balanced_index(p)
    u = p[:idx+1]
    v = p[idx+1:]
    #올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    #올바른 괄호 문자열이 아니라면, 아래과정 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer