from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
color = [0] + list(map(int, input().split()))
visited = [False for _ in range(n+1)]
tree = [[] for _ in range(n+1)]#헷갈리지 말자!!!
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
cnt = 0

def change(start):
    global cnt
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        parent = que.popleft()

        for i in tree[parent]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                #부모와 자식의 색이 다르다면 무조건 색칠하기
                if color[i] != color[parent]:
                    cnt += 1

if color[1] != 0:
    #첫 시작노드를 검사해주지 못함 -> 따로 1 더해주기
    cnt += 1
change(1)
print(cnt)

    

