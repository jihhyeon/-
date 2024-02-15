"""import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n,m,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] + [[2] * m]
sol = [i for i in range(m)]
sol = list(combinations(sol, 3))
print(sol)

# 2. D이하인 적 고르기, 그 중 가장 가까운 적, 여럿일 경우 -> 가장 왼쪽
def choose(s1, s2, s3):
    global d, arr1, attack
    # 궁수 한명마다 하나의 적 공격
    que = deque([s1,s2,s3])
    enemy = []
    while que:
        so = que.popleft() # [n+1][so]
        cnt = 0
        print(so)
        # print(cnt)
        # 적이 있는 행
        for i in range(d):
            print(i)
            idx = n - (d + 1) # 궁수있는 위치 - 거리(1부터 ~ d까지)
            # 적이 있는 열 (idx행의 모든 열 탐색) -> [idx][j]
            for j in range(m):
                if abs(n+1-idx) + abs(so-j) <= d+1:
                    enemy.append([idx, j])
                break
            break
    attack += len(enemy) # 공격당한 적의 수에 추가하기
    print(enemy)
    return attack, enemy
    
# def move(arr1):
#     for i in range(n):
#         for j in range(m):


for i in range(1):
    attack = 0 # 공격받은 적의 수
    arr1 = copy.deepcopy(arr)
    while True:
        no_enemy = True
        for i in range(n):
            for j in range(m):
                if arr1[i][j] != 0:
                    no_enemy = False
        
        # 4. 적이 없으면 게임 끝
        if no_enemy:
            break

        # 1. 궁수 배치
        attack, enemy_list = choose(sol[i][0],sol[i][1], sol[i][2])
        # print('attack', attack)

        # 3. 적 제거하기
        for i,j in enemy_list:
            arr1[i][j] = 0
        
        # 4. 적 이동하기
        # move(arr1)
"""
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M, D = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [0, -1, 0]
dy = [-1, 0, 1]


def kill(archor):
    temp_matrix = [x[:] for x in matrix]

    killed = [[0] * M for _ in range(N)]
    result = 0
    #적군 움직이는 턴 (한칸씩 내려가는거를 for문을 반대로 돌리는 거로 생각)
    for i in range(N-1, -1, -1):
        #이번턴 죽는 애(궁수들이 한번에 공격하니까)
        this_turn = []
        #각 궁수별로 bfs 돌리면서 사정거리 안 제일 가까운 적군 찾기
        for ay in archor:
            #첫 값은 궁수 바로 위 칸으로 넣어줌
            dq = deque([(i, ay, 1)])
            while dq:
                x, y, d = dq.popleft()
                if temp_matrix[x][y] == 1:
                    this_turn.append((x, y))
                    if killed[x][y] == 0:
                        killed[x][y] = 1
                        result += 1
                    break
                if d < D:
                    for di in range(3):
                        nx = x + dx[di]
                        ny = y + dy[di]
                        if 0 <= nx < N and 0 <= ny < M:
                            dq.append((nx, ny, d+1))
        #한 턴에 공격한 애들 한번에 죽이기
        for x, y in this_turn:
            temp_matrix[x][y] = 0
                
    return result

answer = 0

archor_pos = list(combinations([i for i in range(M)], 3))
for a in archor_pos:
    answer = max(answer, kill(a))

print(answer)