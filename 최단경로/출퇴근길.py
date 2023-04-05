import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[]]
for _ in range(m):
    a,b = map(int, input().split())
    graph.append([a,b])
s,t = map(int, input().split())

def search_graph(x,y,graph,stop,start):
    que = deque()
    que.append([x,y])#1,2
    result = []
    while que:
        a,b = que.popleft()#1,2/ 2,4
        for i in range(len(graph)):#[(2,1),(2,3)]
            if graph[i][0] == b:
                if graph[i][1] == stop:#t이면
                    result.append(graph[b][i][0])
                elif graph[i][1] == start or graph[i][1] == a:#다시 출발점이거나 이전 노드와 같으면 무시
                    continue
                else:
                    que.append(graph[i])
            else:
                continue
    return result

print(graph)
for i in range(1, n+1):#1,2,3,4,5
    print(graph[i])
    if graph[i][0] == s:#출발시(1,2), (1,3)
        st_list = search_graph(graph[i][0], graph[i][1], graph,t,s)
    elif graph[i][0] == t:#퇴근시
        fi_list = search_graph(graph[i][0], graph[i][1], graph,s,t)
print(st_list, fi_list)
union = set(st_list) & set(fi_list)
print(union)