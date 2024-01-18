import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(m):
    graph[i] = sorted(graph[i], reverse = True)

numdict = dict()
for i in range(1,n+1):
    numdict[i] = 0

cnt = 1
numdict[r] = 1

def dfs(x):
    global visited, graph, cnt
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            cnt += 1
            numdict[i] = cnt
            dfs(i)

dfs(r)

for i in range(1,n+1):
    print(numdict[i])
