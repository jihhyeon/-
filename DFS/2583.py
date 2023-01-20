#재귀활용 문제 : import sys 꼭쓰기
import sys
sys.setrecursionlimit(1000000)
N,M,K = map(int, input().split())#세로, 가로, 직사각형 개수 / 5,7,3
graph = [[0]*M for _ in range(N)]#초기 0으로 설정
dx = [0,0,-1,1]
dy = [-1,1,0,0]#상하좌우    
cnt = 1#0인 직사각형 개수
res = []

def dfs(x,y,cnt):
    graph[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >=N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 0:
            cnt = dfs(nx,ny,cnt+1)
    return cnt
    
#사각형 영역
for i in range(K):#직사각형 개수만큼 실행
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1, y2):
                graph[j][i] = 1#(N,M)순서로 좌표 표시되기 때문에
                
for i in range(N):#가로만큼 실행
    for j in range(M):
        if graph[i][j] == 0:
            res.append(dfs(i,j,cnt))
            
print(len(res))
print(*sorted(res))
print(res)