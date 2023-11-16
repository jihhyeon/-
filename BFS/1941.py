import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs로 7명의 여학생이 붙어있는지 확인하기
def bfs(arr):
    visited = [[1]*5 for _ in range(5)]

    # 7명의 여학생 위치를 0으로 초기화
    for i in arr:
        visited[i[0]][i[1]] = 0
    
    # 첫번째 여학생의 위치를 큐에 넣음
    que = deque([(arr[0])])
    # 첫번째 여학생의 방문처리를 1로 변경
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1 # 여학생들의 위치 방문 횟수 (첫 위치 방문했기 때문에 1)
    
    while que:
        a,b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                # 만약 위치를 이동하다 아직 여학생 위치를 방문 안했다면
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    check += 1
                    que.append([nx,ny])
    # 7번 다 방문하지 않았다면
    if check != 7:
        return False
    else:
        return True

# dfs에서 7명이고, s>=4인 모든 조합 찾기
def dfs(depth, start, count):
    global result

    # 임도연파가 4명 이상이라면, 재귀탈출
    if count >= 4:
        return

    # 7명을 뽑았다면, 모든 여학생들이 붙어있다면, 1회 추가
    if depth == 7:
        if bfs(arr):
            result += 1
        return 

    for i in range(start, 25):
        r = i // 5 # 총 25번 중 행은 r과 같음
        c = i % 5 # 총 25번 중 열은 c와 같음
        arr.append((r,c))# 해당 위치를 추가
        print(arr, i)
        dfs(depth + 1, i + 1, count + (students[r][c] == 'Y')) #students[r][c] == 'Y'이면 1, 아니면 0임
        arr.pop()


students = [list(map(str, input().rstrip())) for _ in range(5)]
arr = []
result = 0
dfs(0,0,0)
print(result)