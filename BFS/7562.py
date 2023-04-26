"""
중요!! 이동칸수를 갱신하는 그래프 만들기 -> 순차적으로 현재 이동칸수 = 전이동칸 횟수 + 1해주기
"""
from collections import deque

n = int(input())
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x, y):
    visited[x][y] = 1
    que = deque()
    que.append([x,y])
    
    while que:
        a, b = que.popleft()
        if a == after[0] and b == after[1]:
            print(check[after[0]][after[1]])
            break
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<m and 0<=ny<m and visited[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = check[a][b] + 1#전 이동칸횟수 + 1해주기
                que.append([nx,ny])



for _ in range(n):
    m = int(input())#한 변의 길이
    now = list(map(int, input().split()))#현재있는 칸
    after = list(map(int, input().split()))#이동하려는 칸
    check = [[0]*m for _ in range(m)]#각자리에 이동횟수 표시
    visited = [[0]*m for _ in range(m)]

    if now[0] == after[0] and now[1] == after[1]:
        print(0)

    else:
        bfs(now[0],now[1])
    
