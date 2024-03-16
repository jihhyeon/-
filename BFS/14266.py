from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
d = [[-1] * (n+1) for _ in range(n + 1)]

def sol():
    q = deque([(1,0)]) # 현재 화면에 띄워진 개수와 클립보드 개수
    d[1][0] = 0
    while q:
        s, c = q.popleft() # 현재 화면에 띄워진 개수와 클립보드 개수
        print(s,c)
        if s == n:
            print(d[s][c])
            print(d)
            exit()
        # 방문하지 않았으면, 복사 (s,c) -> (s,s)
        if s <= n and d[s][s] == -1:
            d[s][s] = d[s][c] + 1
            q.append((s,s))
        
        # 붙여넣기 (s,c) -> (s+c, c)
        if s + c <= n and d[s+c][c] == -1:
            d[s+c][c] = d[s][c] + 1
            q.append((s+c, c))

        # 하나 삭제하기 (s,c) -> (s-1,s)
        if s - 1 >= 0 and d[s-1][c] == -1:
            d[s-1][c] = d[s][c] + 1
            q.append((s-1,c))
        
sol()