import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
node = dict()
count = 1

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순!!!! -> 이렇게 해야 런타임 에러 안뜸
for i in range(1, n+1):
    graph[i] = sorted(graph[i])

for i in range(n):
    node[i+1] = 0 # i번째 노드의 순서 기록

def dfs(x):
    global graph, visited, node, count
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            count += 1 # 순서 더해주고
            node[i] = count # i번째 노드 순서 기록하기
            dfs(i)
node[r] = 1
dfs(r)

# 마지막 출력
for i in range(n):
    print(node[i+1])
