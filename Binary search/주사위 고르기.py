from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    dic = {}
    L = len(dice)
    
    # 1. a와 b 리스트 구분하기
    for a_index_combi in combinations(range(L), L//2):
        b_index_combi = [i for i in range(L) if i not in a_index_combi]
        A, B = [], []
        for order_product in product(range(6), repeat = L//2):
            A.append(sum(dice[i][j] for i,j in zip(a_index_combi, order_product)))
            B.append(sum(dice[i][j] for i,j in zip(b_index_combi, order_product)))
        B.sort() # 이분탐색을 위한 정렬 수행
        
        # 2. 이분탐색 진행
        wins = sum(bisect_left(B, num) for num in A)
        dic[wins] = list(a_index_combi)
    max_key = max(dic.keys())
            
    return [x+1 for x in dic[max_key]]