n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]#1번노드부터 각 노드로 향하는 거리
ans = 0
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print('graph', graph)

def dfs(cur):
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
            distance[next] = distance[cur] + 1
            dfs(next)

dfs(1)

#리프노드 찾아주기(루트노드는 제외 = 2부터 시작)
for i in range(2, n+1):
    if len(graph[i]) == 1:
        ans += distance[i]#리프노드에 해당하는 거리만 더하기

if ans % 2 == 0:
    print("No")
else:
    print("Yes")