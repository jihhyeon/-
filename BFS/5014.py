import sys
from collections import deque
input = sys.stdin.readline
f,s,g,u,d = map(int, input().split())
visited = [0 for _ in range(f+1)]
count = [0 for _ in range(f+1)]#층수마다 버튼 누른 개수 적립

def bfs(s):
    que = deque()
    que.append(s)
    visited[s] = 1
    while que:
        a = que.popleft()
        if a == g:
            return count[g]
        for i in (a+u, a-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[a] + 1
                que.append(i)
    if count[g] == 0:
        return "use the stairs"

print(bfs(s))