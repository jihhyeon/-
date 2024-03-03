"""
x = 바다, 숫자 = 무인도 -> 상하좌우로 연결되는 땅 = 하나의 무인도
상하좌우로 연결되는 칸에 적힌 숫자를 모두 합한 값 = 해당 무인도에서 최대 머무를 수 있는 날\
각 섬에서 머물수 있는 최대 일수 -> 오름차순으로 return 
만약 지낼 수 있는 무인도 x ; -1담아 return
--------------
bfs로 풀기 / 
"""
from collections import deque
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def solution(maps):
    def island(i, j):
        visit[i][j] = 1
        q = deque()
        q.append([i, j])
        days = 0
        while q:
            i, j = q.popleft()
            days += int(maps[i][j])
            for d in range(4):
                x, y = i + dx[d], j + dy[d]
                if not(0 <= x < n and 0 <= y < m): continue
                if visit[x][y] == 0 and maps[x][y] != 'X':
                    q.append([x, y])
                    visit[x][y] = 1
        return days

    answer = []
    # for i in range(len(maps)):
    #     maps[i] = list(maps[i])#문자열을 리스트로 반환하기
    n = len(maps)
    m = len(maps[0])
    visit = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                answer.append(island(i, j))
    if answer:
        return sorted(answer)
    else:
        return [-1]