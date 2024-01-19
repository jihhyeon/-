from collections import defaultdict
def solution(edges):
    answer = [0,0,0,0]
    dic = dict()
    for a, b in edges:
        if not dic.get(a):
            dic[a] = [0,0]
        if not dic.get(b):
            dic[b] = [0,0]
        # {a정점 : [a정점에서 나가는 간선, a정점으로 들어온 간선] }
        dic[a][0] += 1 # a가 b에게 준 것
        dic[b][1] += 1 # b가 a에게 받은 것
        print(dic)
    
    for key, take in dic.items():
        # 생성한 정점 : 2개 이상 주고, 받는건 없음 = 전체 그래프 개수
        if take[0] >= 2 and take[1] == 0:
            answer[0] = key
        # 막대그래프 : 받는것만 있음
        elif take[0] == 0 and take[1] > 0:
            answer[2] += 1
        # 8자 그래프 : 준 것, 받은 것 각각 2개 이상
        elif take[0] >= 2 and take[1] >= 2:
            answer[3] += 1
            
     # 도넛 : 생성점의 준 개수(전체 그래프 개수) - 막대 - 8자
    answer[1] = (dic[answer[0]][0] - answer[2] - answer[3])
        
    
    return answer