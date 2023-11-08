import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def dfs(cnt, x, end):
    global min_value

    if cnt == end:
        g1, g2 = deque(), deque()

        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        
        ans1 = bfs(g1)

        if not ans1:
            return # 함수 바로 종료
        
        ans2 = bfs(g2)

        if not ans2:
            return
        
        # g1, g2 모두 인접한 구인지 확인이 되었다면 최소값 확인
        min_value = min(min_value, abs(ans1-ans2))
        return
    
    for i in range(x, n):
        if visited[i]:
            continue


n = int(input())
people = list(map(int, input().split()))
board = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        board[i].append(j-1)

min_value = float('inf')
for i in range(1, n//2 + 1):
    visited = [False for _ in range(n)]
    dfs(0,0,i)