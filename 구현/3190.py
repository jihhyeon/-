"""
사과를 먹으면 : 뱀 길이가 늘어남
벽 또는 자기 자신과 부딪히면 게임이 끝남
뱀은 처음에 오른쪽을 향함, 맨위좌측(사과없음)에서 시작, 뱀길이 = 1, 
1. 보드의 크기, 2. 사과개수k 3. k개줄에 사과의 위치(행, 열), 4. 뱀의 방향 변환횟수L, 
5. 뱀의 방향변환 정보(정수, 문자)
"""
from collections import deque
n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]
#상우하좌
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

d = int(input())
dirdict = dict()
queue = deque()
queue.append([0,0])

#방향은 dict로 저장하기
for i in range(d):
    x, c = input().split()
    dirdict[int(x)] = c

x, y = 0,0
graph[x][y] = 1
cnt = 1
direction = 0

def turn(alpha):
    global direction 
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    cnt += 1#시작한 뒤 지난 초
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx<0 or nx>=n or ny<0 or ny>=n:
        break
    
    if graph[nx][ny] == 2:
        graph[x][y] = 1
        queue.append([nx,ny])
        if cnt in dirdict:
            turn(dirdict[cnt])
    
    #사과 없다면 이동후 꼬리 제거
    elif graph[nx][ny] == 0:
        graph[nx][ny] = 1
        queue.append([nx, ny])
        a, b = queue.popleft()
        graph[a][b] = 0
        if cnt in dirdict:
            turn(dirdict[cnt])

    else:
        break
print(cnt)