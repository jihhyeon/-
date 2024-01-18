import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apple = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(apple):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2
dx = [0,1,0,-1] # 서남동북 (방향 변경 = 시계방향), 처음엔 오른쪽으로 이동이기 때문에 서쪽이 먼저!
dy = [1,0,-1,0]

L = int(input())
dirdict = dict()
que = deque()
que.append((0,0))

for i in range(L):
    x,c  = input().split()
    dirdict[int(x)] = c

x,y = 0,0
graph[x][y] = 1
time = 0
direction = 0

# 옆으로 이동하기(x,y,방향)
def turn(dir):
    global direction
    if dir == 'L': # 반시계방향 => 기존 방향의 반대 (서북동남)
        direction = (direction - 1) % 4
    else: # 시계방향 => 서남동북
        direction = (direction + 1) % 4
        

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    # 사과
    if graph[x][y] == 2:
        graph[x][y] = 1
        que.append((x, y))
        # 방향변환 dict에 시간이 있으면 방향변환해주기
        if time in dirdict:
            turn(dirdict[time])
    
    # 사과 없을 때, 몸길이를 줄여 꼬리가 위치한 칸 비워주기
    elif graph[x][y] == 0:
        graph[x][y] = 1
        que.append((x,y))
        tx, ty = que.popleft() # 꼬리(앞에있는 것) pop 해주기
        graph[tx][ty] = 0
        if time in dirdict:
            turn(dirdict[time])
    else:
        break
print(time)


