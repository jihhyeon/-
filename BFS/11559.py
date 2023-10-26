import sys
from collections import deque
input = sys.stdin.readline
graph = [list(map(str, input().rstrip())) for _ in range(12)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
total = 0

# 같은색 뿌요가 4개 이상인지 탐색하기
def search(x, y, puyo):
    visited[x][y] = 1
    color = 1 # 같은색의 뿌요 개수
    location = [[x,y]] # 같은색의 뿌요 위치
    que = deque()
    que.append([x,y])

    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0:
                if graph[nx][ny] == puyo:
                    color += 1
                    visited[nx][ny] = 1
                    location.append([nx,ny])
                    que.append([nx,ny])

    # 4개 이상 있는 뿌요 없애기
    if color >= 4:
        for lo in location:
            graph[lo[0]][lo[1]] = '.'
        return True
    else:
        return False

while True:
    # 한바퀴마다의 연쇄
    cnt = 0
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                if visited[i][j] == 0:

                    # 4개 이상의 같은색 뿌요가 있다면
                    check = search(i,j, graph[i][j])

                    if check == True:
                        # 연쇄 추가해주기
                        cnt += 1

                        # 다른 뿌요들 바닥에 떨어뜨리기 !!!!!
                        for i in range(6):
                            rotate_queue = deque()

                            # 밑에서부터 스캔하며 뿌요를 넣어주기
                            for j in range(11,-1,-1):
                                if graph[j][i] != '.':
                                    rotate_queue.append(graph[j][i])

                            # 밑에서부터 뿌요 쌓아주기
                            for j in range(11,-1,-1):
                                if rotate_queue:
                                    graph[j][i] = rotate_queue.popleft()
                                else:
                                    graph[j][i] = '.'

    # 총 연쇄에 추가해주기 (동시에 터지는 것은 한번의 연쇄임)
    if cnt > 0 :
        total += 1
    # 연쇄가 일어나지 않은 경우는 break
    else:
        break

print(total)