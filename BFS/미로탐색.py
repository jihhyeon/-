from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    que = deque()
    que.append([x,y])
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1#w지나야하는 최소칸수 더해주기
                que.append([nx,ny])

    return array[n-1][m-1]

print(bfs(0,0))

# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []

# for _ in range(n):
#     graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함
# print(graph)
# # 상하좌우
# dx = [-1, 1, 0, 0] 
# dy = [0, 0, -1, 1]

# def bfs(x, y):
    
#     queue = deque()
#     queue.append((x,y))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = graph[x][y] + 1
    
#     return graph[n-1][m-1]

