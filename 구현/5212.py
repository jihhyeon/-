import sys
from collections import deque
import copy
input = sys.stdin.readline

r,c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, input().rstrip())))
new = copy.deepcopy(graph)
array_range = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def count(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny] == ".":#상하좌우 바다면 cnt + 1
                cnt += 1
        else:#범위 밖은 무조건 바다이므로 cnt + 1
            cnt += 1

for i in range(r):
    for j in range(c):
        if graph[i][j] == "X":
            cnt = 0
            count(i,j)
            if cnt >= 3:
                new[i][j] = "."

for i in range(r):
    for j in range(c):
        if new[i][j] == "X":
            array_range.append([i,j])
a = []
b = []
for i in range(len(array_range)):
    a.append(array_range[i][0])
    b.append(array_range[i][1])

h_a, h_b = min(a), max(a)
y_a, y_b = min(b), max(b)

for i in range(h_a,h_b+1):
    for j in range(y_a,y_b+1):
        print(new[i][j], end = '')
    print()


        


