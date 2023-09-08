import sys
sys.setrecursionlimit(10**5)
def dfs(i,j):#2가지 경우로 나뉘는걸 체크해주기 위한 함수.
    for k in range(4):
        nx = dx[k]+i
        ny = dy[k]+j
        if 0<=nx<n and 0<=ny<m and vist[nx][ny]:
            vist[nx][ny]=False
            if s[nx][ny]!=0:
                dfs(nx,ny)
            

input = sys.stdin.readline
n,m = map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
vist = [[False]*m for _ in range(n)]#방문 체크
t = 0

while True:
    t+=1
    for i in range(n):#빙하를 녹이는 함수
        for j in range(m):
            if s[i][j]!=0:
                vist[i][j] = True #앞서 말한 경우를 방지해주기 위한 작업
                c=s[i][j]
                for k in range(4):
                    nx = dx[k]+i
                    ny = dy[k]+j
                    if 0<=nx<n and 0<=ny<m and not vist[nx][ny]:
                        if s[nx][ny]==0:
                            c-=1
                            if c==0:#음수가 되면 안 되니 dfs작업을 멈춰준다.
                                break
                s[i][j]=c#녹은 빙하를 저장해줌
                
    ch=0#영역의 개수
    for i in range(n):
        for j in range(m):#방문체크 배열을 재사용하기 위해 True->False로 다 고쳐준다.
            if s[i][j]!=0 and vist[i][j]:
                dfs(i,j)#영역을 체크한다.
                ch+=1
            elif s[i][j]==0 and vist[i][j]:
                vist[i][j]=False
                
    if ch>=2:#영역이 2개 이상으로 나뉜경우니 출력해주고 반복문을 탈출한다.
        print(t)
        break
    elif ch==0:#한번에 녹았다는 의미이므로 0을 출력해주고 반복문을 탈출한다.
        print(0)
        break