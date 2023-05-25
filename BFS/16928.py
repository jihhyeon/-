import sys
from collections import deque
n, m = map(int, input().split())
#딕셔너리로 구현하기
ladder = dict()
snake = dict()
for _ in range(n):
    a,b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a,b = map(int, input().split())
    snake[a] = b

board = [0] * 101#주사위 굴린 횟수 넣어주는 리스트!!!!
visited = [0] * 101

que = deque([1])

while que:
    x = que.popleft()
    if x == 100:
        print(board[x])
        break
    for dice in range(1,7):
        next = x + dice
        #범위안에 있고 아직 방문하지 않았다면
        if next <= 100 and visited[next] == 0:
            #사다리가 있다면
            if next in ladder.keys():
                next = ladder[next]
            #뱀이 있다면
            if next in snake.keys():
                next = snake[next]
            #아무것도 없다면
            if visited[next] == 0:
                visited[next] = 1#방문표시
                board[next] = board[x] + 1#주사위 굴린 횟수 추가
                que.append(next)
    
