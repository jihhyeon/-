from collections import deque
import sys
def solution(maps):
    ans = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    remap = []
    final = True
    for i in maps:
        remap.append(list(map(str, i.rstrip())))
            
    # 2. 최소시간 -> 모든 간선의 길이가 같을 때 : bfs이용해 최단거리 찾기
    def bfs(target, x, y):
        visited = [[0]* len(maps[0]) for _ in range(len(maps))]
        que = deque()
        que.append([x,y])
        while que:
            a, b = que.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0:
                    if remap[nx][ny] != 'X':
                        # 통로, 출구, 시작점이면 (이들은 여러번 지나갈 수 있음)
                        if remap[nx][ny] != target:
                            visited[nx][ny] = visited[a][b] + 1
                            que.append([nx,ny])
                        # target이면
                        else:
                            visited[nx][ny] = visited[a][b] + 1
                            return [visited[nx][ny], nx, ny]

        
    # 1. 시작은 s칸에서
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if remap[i][j] == 'S':
                a = bfs('L',i,j) # 찾아야하는 레버, 위치
                if not a:
                    final = False
                else:
                    loca, x, y = a[0], a[1], a[2]
                    ans += loca
                    b = bfs('E',x,y)
                    if not b:
                        final = False
                    else:
                        loca, x, y = b[0], b[1], b[2]
                        ans += loca
    
    if final == False:
        return -1
    else:
        return ans
