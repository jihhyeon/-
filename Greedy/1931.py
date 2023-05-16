import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
#이 문제의 포인트!
graph.sort(key = lambda x: (x[1], x[0]))#끝나는 시각, 시작 시각 순서로 오름차순 정렬

cnt = 1
end_time = graph[0][1]
for i in range(1, n):
    if graph[i][0] >= end_time:
        cnt += 1
        end_time = graph[i][1]
print(cnt)