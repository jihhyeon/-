from itertools import combinations_with_replacement
# k점에 여러발 쏠 수 있으니 반복이 있어야함

def solution(n, info):
    answer = [-1]
    max_gap = -1 # 점수 차
    
    for combi in combinations_with_replacement(range(11), n):
        info2 = [0]*11
        
        for i in combi:
            info2[10 - i] += 1 # 10점부터 점수 넣기
            
        apeach, lion = 0,0
        # 어피치와 라이언 화살 비교
        for idx in range(11):# idx = 0,1,2,3,4,...
            # 어피치와 라이언 모두 한번도 화살을 맞히지 못한 경우
            if info[idx] == info2[idx] == 0:
                continue
            # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌경우
            elif info[idx] >= info2[idx]:
                apeach += 10 - idx
            # 라이언이 어피치보다 많은 수의 화살을 맞힌 경우
            else:
                lion += 10 - idx
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    return answer
            