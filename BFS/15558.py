from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(2)]
visited = [[False] * n for _ in range(2)]
visited[0][0] = True

# 1. 앞, 뒤, i+k가 1인지 탐색하기
def bfs():
    i = 0 # 인덱스
    que = deque([(i,0,0)]) # 인덱스, 위치(왼,오른), 시간

    while que:
        i, pos, t = que.popleft()
        dx = [1,-1,k]

        for j in range(3):
            nx = i + dx[j]

            if nx >= n:
                return print(1)
            
            # 앞, 뒤
            if t < nx and map[pos][nx] == 1 and j != 2:
                if not visited[pos][nx]:
                    visited[pos][nx] = True
                    que.append((nx,pos,t+1))
            
            # i+k칸 앞, 반대
            elif t < nx and map[1-pos][nx] == 1 and j == 2: # 1-pos = 반대칸(왼,오른)
                if not visited[1-pos][nx]:
                    visited[1-pos][nx] = True
                    que.append((nx, 1-pos, t+1))

    print(0)

bfs()