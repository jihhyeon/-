from collections import deque

n, k = map(int, input().split())
max = 100000
visited = [0]*(max +1)#방문횟수 표시해주는 리스트 만들기

def bfs():
    q = deque()
    q.append(n)#수빈이 출발점 위치 큐 삽입
    while q:
        x = q.popleft()
        #수빈이 위치가 동생의 위치와 같다면 반복문 종료
        if x == k:
            print(visited[x])
            break
        #이동할 수 있는 방향에 대해
        for j in (x-1, x+1, x*2):
            #주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0<=j<=max and not visited[j]:
                #이동한 위치에 현재 이동한 시간 표시
                visited[j] = visited[x]+1
                q.append(j)

bfs()
