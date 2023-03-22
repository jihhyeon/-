#바이러스는 상하좌우로 퍼져나감, 세울 수 있는 벽의 개수=무조건 3개, 0=빈칸 1=벽 2=바이러스
#안전영역(바이러스가 퍼질 수 없는 곳)의 크기를 최대로하기
#1. 벽 3개를 꼭 세우기
#2. 바이러스는 상하좌우 인접한 칸으로 이동 -> bfs 사용
#3. 바이러스의 위치를 전부 큐에 넣고 while queue 돌리기
#4. 바이러스를 퍼트린 후 0이 몇개있는지 세고, 최대값을 찾는다.
from collections import deque
import copy
lab_map = [
    [2,0,0,0,1,1,0], 
    [0,0,1,0,1,2,0], 
    [0,1,1,0,1,0,0], 
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0]
]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#벽을 설치하면서 매번 안전거리 계산
def bfs():
    queue = deque()
    #queue에 2의 위치 전부 append
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 2:
                queue.append([i,j])
    
    while queue:
        a,b = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<n and 0<=ny<m:
                if test_map[nx][ny] == 0:
                    test_map[nx][ny] = 2#바이러스 퍼트리기
                    queue.append([nx,ny])

    global result
    count = 0
    #안전영역 개수 세기
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                count += 1
    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0:
                lab_map[i][j] = 1
                make_wall(count + 1)
                lab_map[i][j] = 0#다시 0으로 돌려주기

n, m = map(int,input().split())

result = 0
make_wall(0)

print(result)      