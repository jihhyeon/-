"""import sys
from itertools import permutations, combinations
input = sys.stdin.readline
n, k = map(int, input().split())
bag = []
for _ in range(n):
    a, b = map(int, input().split())
    bag.append([a,b])
bags = []
for i in range(1,5):
    bags += list(combinations(bag, i)) # 모든 경우에 대한 조합
value = 0 # 최대값으로 갱신하기

for baglist in bags:
    weight = k
    val = 0
    while True:
        for w,v in baglist:
            weight -= w # 남은 무게
            if weight >= 0: # 남은 무게가 0이상이면 가치 더하기
                val += v
            else: # 남은 무게가 0 
                break # for문 빠져나오기
        break # while문 빠져나오기
    value = max(val, value) # 최대값으로 갱신해주기
print(value)
                """
import sys
input = sys.stdin.readline
 
N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
dp = [0 for _ in range(K + 1)]
print(items)

for w,v in items:
    print(w, v)
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp[-1])



