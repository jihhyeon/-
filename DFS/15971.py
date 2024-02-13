# 동굴의 방 개수 n, 두 로봇이 위치한 방의 번호
# 동굴의 통로 n-1개 => 통로의 양 끝에 위치한 방의 번호, 그 통로의 길이
import sys
from collections import deque

input = sys.stdin.readline
n, start, end = map(int, input().split())
room = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    room[a].append([b,c])
    room[b].append([a,c])
print(room)

def solv():
    visited = [False] * (n+1)
    q = deque([(start, 0,0)])
    visited[start] = True

    while q:
        now, total, max_cost = q.popleft() # 지금 위치, 전체 경로 길이, 가장 긴 통로
        print(now, total, max_cost)
        if now == end:
            print(total - max_cost) # 전체 경로 - 가장 긴 통로
            return
        print('room now', room[now])
        for nxt, cost in room[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, total+cost, max(max_cost, cost)))

solv()
    
