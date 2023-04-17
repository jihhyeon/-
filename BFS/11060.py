from collections import deque
import sys
input = sys.stdin.readline
# n = 10
# # graph = deque(list(map(int, input().split())))
# graph = deque([1, 2, 0, 1, 3, 2, 1, 5,4,2])
# visited = [0]*n
# cnt = 0
# idx = 9
# while True:
#     if len(graph) == 0:
#         break
#     minus = abs(idx - graph[0])#8 = 9-1, 6 = 8-2, ..., -3 = 2-5
#     real_minus = idx - graph[0]
#     print(real_minus)

#     if len(graph) != 0 and real_minus == 0:
#         print(graph, real_minus)
#         break

#     else:
#         for i in range(graph[0]):
#             if len(graph) == 0:
#                 break
#             visited[minus - (i+1)] = 1
#             graph.popleft()#[2,0,1,3,2,1,5,4,2]
#         idx = minus#8
#         cnt += 1
# print(visited)
# if visited[-1] == 0:
#     print('-1')
# else:
#     print(cnt)

"""----------------------------"""
n = int(input())

#1이라면 시작과 동시에 종료
if n == 1:
    print(0)
    sys.exit()

arr = list(map(int, input().split()))
visited = [0]*n
q = deque([(0, arr[0])])#현재 위치, 점프 가능 거리

while q:
    pos, jump = q.popleft()
    for i in range(1, jump+1):
        if pos+i >= n or visited[pos+i]:#현재거리 + i가 n보다 크거나, 방문했다면
            continue
        visited[pos+i] = visited[pos]+1#몇번 점프하는지 추가하기
        q.append((pos+i, arr[pos+i]))
print(visited)
print(visited[-1] if visited[-1] else -1)
