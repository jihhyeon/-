import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N,R=map(int,input().split())
Tree=[ [] for _ in range(N+1) ]


def DFS(start,count):
    global First,New_start,leaf_check
    check=[]
    visit[start]=True
    for i,j in Tree[start]:
        if not visit[i]:
            check.append([i,j])
            leaf_check+=j
            print(check, leaf_check)

    if len(check)>=2:
        First=count ; New_start=start
        return
    else:
        if check:
            DFS(check[0][0] , count+check[0][1])

def DFS2(start,count):
    global ans
    visit[start]=True
    for i,j in Tree[start]:
        if not visit[i]:
            ans=max(ans,count+j)
            DFS2(i,count+j)


for i in range(N-1):
    a,b,d=map(int,input().split())
    Tree[a].append([b,d])
    Tree[b].append([a,d])

visit=[False]*(N+1)
First=0 ; New_start=-1 ; ans=0 ; leaf_check=0

DFS(R,0)

DFS2(New_start,0)

if New_start==-1:
    print(leaf_check,ans)
else:
    print(First,ans)