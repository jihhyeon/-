"""바이러스 종류 = 1~k번, 모든 바이러스는 1초마다 상하좌우 증식(매초 번호가 낮은 종류의 바이러스부터 증식)
증식과정 -> 특정 칸에 이미 바이러스 존재하면 다른 바이러스 들어갈 수 없음
s초가 지난 후 (x,y)에 존재하는 바이러스의 중류를 출력하기, 만약 해당 위치에 바이러스 존재 x-> 0출력하기
--------------------
1. k번 반복문하여 낮은 숫자부터 상하좌우 증식해주기
2. 이미 바이러스 존재하면 숫자 넣지 않기
"""
from collections import deque
# import copy

# n,k = map(int, input().split())
# graph = []
# visited = [[0]*n for _ in range(n)]
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())#-> 1부터 시작이니까 출력부분에서 각각 -1 해주기(인덱스)
# answer = copy.deepcopy(graph)#원래 리스트인 graph에 아무 영향을 미치지 않음

# def bfs(x, y, vir, answer):
#     visited[x][y] = 1
#     que = deque()
#     que.append([x,y])
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     while que:
#         a, b = que.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = a + dy[i]
#             if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
#                 answer[nx][ny] = vir
#                 visited[nx][ny] = 1

#     return answer


# for time in range(s):#매 초마다 반복
#     for vir in range(1, k+1):#1,2,3 : 바이러스 종류
#         for i in range(n):#0,1,2
#             for j in range(n):#0,1,2
#                 if graph[i][j] == vir:
#                     answer = bfs(i, j, vir, answer)#그래프 반환하고, 재설정
#                 else:
#                     continue
# if answer[x-1][y-1] == 0:
#     print(0)
# else:
#     print(answer[x-1][y-1])
#-------------------------시간초과뜸
#for문의 개수를 줄여보자..
n,k = map(int, input().split())
graph = []
data = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))
s, x, y = map(int, input().split())#-> 1부터 시작이니까 출력부분에서 각각 -1 해주기(인덱스)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

data.sort()
print(data)
que = deque(data)

while que:
    virus, x, y, time = que.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            que.append((virus, nx, ny, time + 1))
print(graph[x-1][y-1])