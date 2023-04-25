"""1.i -> j로 가는 경로가 있다면, j->i도 경로 있음
2. (0,0) = (0,1) -> (1,0) 으로 해결할 수 있음 [플로이드 워셜 알고리즘..]
"""
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            print(k,i,j)
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end = " ")
    print()