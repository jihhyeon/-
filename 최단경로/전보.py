import heapq
n,m,c = map(int, input().split())#도시개수, 통로개수, 메세지를 보내는 도시
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)#최단 거리 저장

for a in range(1,n+1):
    for b in range(1, n+1):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))#노드, 거리
start = c

def dijstra(start):
    q = []
    heapq.heappush(q,(0,start))#거리, 노드
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)#거리, 노드
        #이미 방문했거나, 현재값(dist)이 이전 값보다 클 때
        if distance[now] < dist:
            continue
        for i in graph[now]:#(노드, 거리)
            cost = dist + i[1]#dist + 거리
            if cost < distance[i[0]]:#cost < distance[노드]
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)