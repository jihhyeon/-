import sys

sys.setrecursionlimit(1000000)

def dfs(x,y,land):
    global cnt, oil, dx, dy, n, m, visited
    visited[x][y] = True
    land[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
            oil += 1
            dfs(nx, ny, land)
    return oil
    
def solution(land):
    global cnt, oil, dx, dy, n, m, visited
    answer = 0
    cnt = 2 # 덩어리 개수
    total = {}
    n, m = len(land), len(land[0])
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    visited = [[False] * m for _ in range(n)]
    
    # 1. 덩어리 구분하기
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                oil = 1 # 석유량
                dfs(i,j, land)
                
                # 2. 석유량 넣어주기
                total[cnt] = oil
                cnt += 1
#     print(land)
#     print(total)
    
    # 3. 시추관 넣기        
    for j in range(m):
        # 열의 유일한 값들
        oil_types = set([land[i][j] for i in range(n)])
        amount = 0
        for am in oil_types:
            if am in total.keys():
                amount += total[am]
        answer = max(amount, answer)
    
    return answer
# from queue import deque
# from collections import defaultdict

# directions = (0, 1, 0, -1, 0)

# def bfs(i, j, n, m, oil, land):
#     amount = 1
#     land[i][j] = oil
#     que = deque([(i, j)])
#     while que:
#         x, y = que.popleft()
#         for d in range(4):
#             nx, ny = x + directions[d], y + directions[d+1]
#             if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
#                 amount += 1
#                 land[nx][ny] = oil
#                 que.append((nx, ny))
                
#     return amount

# def solution(land):
#     answer, oil = 0, 2
#     n, m = len(land), len(land[0])
#     amount_of = defaultdict(int)

#     for i in range(n):
#         for j in range(m):
#             if land[i][j] == 1:
#                 amount_of[oil] = bfs(i, j, n, m, oil, land)
#                 oil += 1
#     print(amount_of)
                
#     for j in range(m):
#         oil_types = set([land[i][j] for i in range(n)])
#         print(oil_types)
#         amount = 0
#         for oil in oil_types:
#             amount += amount_of[oil]
#         print(amount)
#         answer = max(amount, answer)
    
#     return answer