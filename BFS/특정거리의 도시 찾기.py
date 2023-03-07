#x도시에서 출발, 최단 거리가 = k 인 모든 도시의 번호를 출력(한줄씩 오름차순)
#단, 최단거리가 k인 도시가 하나도 존재하지 않으면 -1 출력
from collections import deque
n, m, k, x = map(int, input().split())
#편하게 도시 1부터 확인하기 위해 그래프 0번째 칸은 빈칸으로 생성
graph = [[] for _ in range(n+1)]
answer = []
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
print(graph)

distance = [-1]*(n+1)#방문하지 않은 도시는 -1
distance[x] = 0#출발도시는 0으로 설정

que = deque()
que.append(x)#출발지 1 삽입
print(que)
while que:
    now = que.popleft()#now = 1
    for next in graph[now]:#[2,3], [3,4]
        #아직 방문하지 않은 도시라면
        if distance[next] == -1:#distance[2] = -1, distance[3] = -1
            #최단거리 갱신
            #현재 도시와 출발도시 사이의 거리 +1
            distance[next] = distance[now]+1#distance[2] = 1, distance[3] = 1
            que.append(next)
            print(next, que)
check = False
print(distance)
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
    
    





# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == x:
#             answer.append([j, dfs(graph,i,j)])#횟수

