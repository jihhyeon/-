INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]#노드가 1부터 시작되기 때문
answer_1 = []
answer_2 = []
#연결된 두 회사
for _ in range(m):
    a, b = map(int, input().split())
    #a와 b가 서로에게 가는 비용은 1이라고 설정
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

#자기자신 -> 자기자신 = 0처리해주기
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#수행한 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)