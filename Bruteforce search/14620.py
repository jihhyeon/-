"""n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

check = [[0]*(n-2) for _ in range(n-2)]
visited = [[0]*(n-2) for _ in range(n-2)]
ans = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def count(x,y):
    check[x-1][y-1] = graph[x][y]
    for i in range(4):
        ix = x + dx[i]#인덱스
        iy = y + dy[i]
        check[x-1][y-1] += graph[ix][iy]

def min_price(x,y):
    find_min = [check[x][y]]
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<(n-2) and 0<=ny<(n-2):
            if visited[nx][ny] == 0:
                find_min.append(check[nx][ny])
                visited[nx][ny] = 1
            elif visited[nx][ny] == 1 and check[nx][ny] <= check[x][y]:
                break
    ans.append(min(find_min))


for i in range(1,n-1):
    for j in range(1,n-1):
        count(i,j)

for i in range(n-2):
    for j in range(n-2):
        min_price(i,j)

ans.sort()
ans = list(set(ans))
price = 0
for i in range(3):
    price += ans[i]

print(price)"""


import sys

def check(i, j, visited):
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj)  in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)

print(answer)