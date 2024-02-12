"""이해 안가는 지문 : 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
이 말은 = 파이어볼이 격자 범위를 넘어가는 것을 방지하기 위한 조건으로, 1번행의 범위가 넘어가면 4번행으로 간다 이말임.
"""
import sys
input = sys.stdin.readline
# 1. 입력
n,m,k = map(int, input().split())
fireballs = []
for _ in range(m):
    rr,cc,mm,ss,dd = list(map(int, input().split()))
    fireballs.append([rr-1,cc-1,mm,ss,dd])
arr = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
ans = 0 # 질량의 총합

for _ in range(k):

    # 1. 파이어볼 이동하기
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs * dx[cd]) % n
        nc = (cc + cs * dy[cd]) % n
        arr[nr][nc].append([cm,cs,cd])
        print(*arr, sep = '\n')

    # 2. 이동 뒤, 2개이상의 파이어볼이 있는 칸에서
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0,0,0,0, len(arr[i][j])
                while arr[i][j]:
                    _m, _s, _d = arr[i][j].pop(0)
                    sum_m += _m
                    sum_s += _s
                    # 방향
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                if sum_m // 5: # 질량이 0이면 소멸
                    for d in nd:
                        fireballs.append([i,j,sum_m//5, sum_s//cnt, d])

print(sum([f[2] for f in fireballs]))

        




