"""1. 치킨집을 기준으로 
2. 
"""
from itertools import combinations
n, m = map(int, input().split())
chicken, house = [], []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append([r,c])
        elif data[c] == 2:
            chicken.append([r,c])
#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

#치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    #모든 집에 대하여
    for hx, hy in house:
        temp = 1e9
        #가장 가까운 치킨집 찾기
        for cx, cy in candidates:
            temp = min(temp, abs(hx-cy)+abs(hy-cy))
        result += temp
    return result
    
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)
