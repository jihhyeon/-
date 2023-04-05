import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())#노드 개수, 간선 개수 입력
start = int(input())#시작 노드 번호 입력
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)#10억

for _ in range(m):
    a,b,c = map(int, input().split())#a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))
#[[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:#큐가 비어있지 않다면
        dist, now = heapq.heappop(q)#거리, 노드 -> 첫번쨰 원소(거리)로 우선순위 판별
        if distance[now] < dist:#이미 처리된 적이 있는 노드라면 무시
            continue
        #현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            print(cost, i[0],distance[i[0]])
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost#노드 인덱스(i[0])에 거리 저장
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])