import sys
from collections import deque
input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cleaner = []

# 1. 공기청정기 위치 받기
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            cleaner.append([i,j])


# 2. 미세먼지 확산
# 미세먼지 퍼뜨리기
def spread():
    tmp_arr = [[0] * c for _ in range(r)]
    # 미세먼지 있는 칸 알아내기
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != 1:
                direction = 0 
                for i in range(4):
                    nx = i + dx[i]
                    ny = j + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += (arr[i][j] // 5)
                        direction += 1
                arr[i][j] = arr[i][j] - (arr[i][j] // 5) * direction
    # 남은 미세먼지 양 계산
    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]
    return

# 3. 반시계 방향으로 이동
def change_up():
    up_step = [[0,1],[-1,0],[0,-1],[1,0]] # 동북서남 방향
    direct = 0
    x,y = cleaner[0] # 공기청정기 윗부분
    up, y = x, 1 # 시작위치 : up(x), y(1)
    previous = 0 # 이전 값
    while True:
        nx, ny = x + up_step[direct][0], y + up_step[direct][1]
        # 처음 위치로 되돌아오면 종료
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        # 두 변수 값 바꾸기
        arr[x][y], previous = previous, arr[x][y]
        # 다음 위치로 이동
        x, y = nx, ny
    return

# 4. 시계 방향으로 이동
def change_down():
    up_step = [[0,1],[1,0],[0,-1],[-1,0]] # 동남서북 방향
    direct = 0
    x,y = cleaner[1] # 공기청정기 아랫부분
    up, y = x, 1 # 시작위치 : up(x), y(1)
    previous = 0
    while True:
        nx, ny = x + up_step[direct][0], y + up_step[direct][1]
        # 처음 위치로 되돌아오면 종료
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        # 두 변수 값 바꾸기
        arr[x][y], previous = previous, arr[x][y]
        # 다음 위치로 이동
        x, y = nx, ny
    return

# 5. T초 후까지 반복
for _ in range(t):
    spread()
    change_up()
    change_down()

# T초 후에 남아있는 미세먼지의 양 총합 계산
ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)


