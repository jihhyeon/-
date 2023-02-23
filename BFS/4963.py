# 1 : 섬, 0 : 바다
# 섬의 개수를 세는 프로그램 작성하기
# 상하좌우, 대각선 모두 걸어갈 수 있는 사각형
# 첫째줄 : 지도 너비, 높이
# 둘째줄 : h개의 줄에는 지도가 주어짐
from collections import deque
import sys
sys.setrecursionlimit(1000000)
# w,h = map(int, input().split())
# graph = [[0]*w for _ in range(h)]
#사선(왼+위, 오+위, 왼+아래, 오+아래)
#dx, dy : -1,1/1,1/-1,-1/1,-1
cnt = 0

#bfs
#첫번째 시작 -> 상하좌우 사선 탐색 -> 1이 있다면 쭉 가기
#                             1이 없다면 멈추고 -> cnt +=1

def bfs(x,y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]#상하좌우+사선
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    graph[x][y] = 0#그래프는 방문처리해주기
    que = deque()
    que.append([x,y])#큐에 넣기
    while que:
        a,b = que.popleft()#넣은 원소 pop하기
        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:#범위안에 있고 1인 경우
                graph[nx][ny] = 0#그래프는 방문처리해주기
                que.append([nx, ny])#1일때, que 계속 돌리게됨


def dfs(x,y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]#상하좌우+사선
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    graph[x][y] =0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:#범위안에 있고 1인 경우
            dfs(nx, ny)

while True:
    w,h = map(int, input().split())
    graph = []
    cnt = 0
    if w == 0 and h == 0:
        break
    #h줄 만큼 입력받기
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):#5
        for j in range(w):#4
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)