import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(x):
    if visited[x] == 0:
        visited[x] = 1#방문처리
        for i in graph[x]:
            dfs(i)
        return True
    return False#방문했었으면 False return

cnt = 0

for i in range(1, n+1):
    if dfs(i) == True:
        cnt += 1

print(cnt)

