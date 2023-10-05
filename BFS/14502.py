from collections import deque
import copy

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def make_wall(x):
    print(x)
    print('make_wall')
    print(graph)
    if x == 3:
        # bfs()
        print("bfs")
        return
    for i in range(2):
        for j in range(2):
            print(i,j)
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(x+1)
                print('zero')
                graph[i][j] = 0
                print(i,j,graph)

make_wall(0)