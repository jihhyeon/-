# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# ## 북, 동, 하, 서 ( 시계방향 )
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def search_clean(x,y):
#     cnt, no_clean, yes_clean = 0,0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             cnt += 1
#             # 청소된 경우
#             if graph[nx][ny] != 0:
#                 no_clean += 1
#             # 청소 안된 경우
#             if graph[nx][ny] == 0:
#                 yes_clean += 1
#     # 모든 곳이 청소된 경우 
#     if cnt == no_clean
#         return True
#     else:
#         return False

# while True:
#     # 1번. 현재칸이 청소되지 않은 경우, 청소하기
#     if graph[r][c] == 0:
#         graph[r][c] = 1
    
#     # 2번. 모든 곳이 청소 된 경우
#     if search_clean(r,c):
#         if 
                
d = 0
d = (d+3)%4
print(d)