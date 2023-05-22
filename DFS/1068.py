import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = -2
    for i in graph[v]:
        dfs(i)

n = int(input())
li = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(1,n):#0번 노드는 root node이기 때문
    graph[li[i]].append(i)#[[1, 2], [3, 4], [], [], []]

# print(graph)
erase = int(input())
visited = [0] * n

dfs(erase)

cnt = 0
for i in range(n):
    if visited[i] != -2 and len(graph[i]) != 0:#삭제되지 않고, 자식노드가 0이 아닌
        cnt += 1

print(cnt)