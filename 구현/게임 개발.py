#(A,B) a = 북쪽으로부터 떨어진 칸의 개수, b = 서쪽으로부터 떨어진 칸의 개수
#상하좌우 움직일 수 있음, 바다로 되어있는 공간에는 갈 수 없음
from collections import deque
n, m = map(int, input().split())#행, 열
x, y, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]
dir = [0,1,2,3]#북, 동, 남, 서
dx = [0,1,0,-1]#북동남서
dy = [-1,0,1,0]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
    
count = 1
turn_time = 0#네방향을 둘러보는지
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        #뒤로 갈 수 있다면 이동하기
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)