import sys
sys.setrecursionlimit(10**6)
n = int(input())
num = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
count = 0

# 1번부터 웜바이러스 걸림
# 연결된 노드를 돌면서 visited = 1로 바꾸고, 방문 안한 노드들 count하기
def dfs(x):
    global count
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            count += 1
            dfs(i)
    
dfs(1)
print(count)