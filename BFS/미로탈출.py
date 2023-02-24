# #벽으로 된 칸 : 지나갈수 x, 통로로 된 칸 : 이동 o
# #레버 : 미로를 빠져나가는 문, 통로들 중 한칸 
# #S : 시작 지점, E : 출구, L : 레버, O : 통로, X : 벽
# #레버를 당기고 -> 출구로 이동
# #미로에서 한칸을 이동하는데 1초-> 최단기간 미로를 빠져나가는데 걸리는 시간 구하기
# #단, s, L, E가 x로 막혀있으면 탈출 못함 -> -1 반환
# #bfs) start부터 시작 -> 상하좌우 o인 곳으로만 이동 -> l만나야함(못만나면 -1반환)
# #-> E에 도달하면 종료
from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps),len(maps[0])
    # 출발 지점
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx,sy = i,j
    # 레버 찾기
    def bfs(x,y,end):
        q = deque()
        q.append([x,y])
        visited = [[-1]*m for _ in range(n)]
        visited[x][y] = 0
        while q:
            dx = [0,0,-1,1]
            dy = [1,-1,0,0]
            x,y = q.popleft()
            if maps[x][y] == end:#해당 상태(L, E)일때 return 하기
                return [visited[x][y],x,y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1:
                        if maps[nx][ny] != 'X':
                            q.append([nx,ny])
                            visited[nx][ny] = visited[x][y] + 1#레버와 출구 나올때까지 계속 1 더해주기
        return None
    cnt = bfs(sx,sy,'L')#시작점~레버까지의 cnt
    if cnt == None:#L이 없을 때 -1 return 
        return -1
    answer += cnt[0]
    cnt = bfs(cnt[1],cnt[2],'E')#레버~출구까지의 cnt
    if cnt == None:
        return -1
    answer += cnt[0]
    return answer