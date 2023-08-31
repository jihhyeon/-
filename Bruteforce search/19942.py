import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
mp,mf,ms,mv = map(int, input().split())

ingradient = [[]]
for _ in range(n):
    p,f,s,v,c = map(int, input().split())
    ingradient.append((p,f,s,v,c))
print(ingradient)

def solv():
    answer_c = 9875643210
    answer = None
    for cnt in range(1, n+1):
        #1~n까지의 숫자를 cnt개의 조합으로 만든것 = comb
        for comb in combinations(range(1,n+1), cnt):
            tp = tf = ts = tv = tc = 0
            for target in comb:
                tp += ingradient[target][0]
                tf += ingradient[target][1]
                ts += ingradient[target][2]
                tv += ingradient[target][3]
                tc += ingradient[target][4]
            if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
                if answer_c > tc:
                    answer_c = tc
                    answer = comb
                    print(answer, answer_c)
                elif answer_c == tc:
                    answer = comb

    if answer_c == 9875643210:
        print(-1)
    else:
        print(answer_c)
        print(*answer)

solv()


