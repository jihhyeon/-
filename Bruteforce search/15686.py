"""
치킨거리 : 집과 가까운 치킨집 사이의 거리
도시의 치킨거리 : 모든 집의 치킨거리"""
# M개를 어떻게 선정할 것인가 => 조합!
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 999999
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i,j])
        if graph[i][j] == 2:
            chicken.append([i,j])
comb = combinations(chicken, m)
print(list(comb))

for chi in comb:
    temp = 0
    # 각 집을 기준점으로 잡기
    for hom in home:
        chi_len = 999
        #각 집에서 치킨집까지의 거리
        for j in range(m):
            chi_len = min(chi_len, abs(chi[j][0] - hom[0]) + abs(chi[j][1] - hom[1]))
        temp += chi_len
    result = min(result, temp)
print(result)