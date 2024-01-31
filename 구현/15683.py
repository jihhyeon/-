import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
cctv = [] # cctv 종류, x좌표, y좌표
board = [] # 사무실 정보
mode = [[], [[0],[1],[2],[3]], [[0,2],[1,3]],[[0,1],[1,2],[2,3],[0,3]],
[[0,1,2],[0,1,3],[0,2,3],[0,2,3]], [[0,1,2,3]]]
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j], i, j])

def fill(board, mode, x, y): # 감시
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            # 감시가능
            elif board[nx][ny] == 0:
                board[nx][ny] = -1

def dfs(depth, board):
    global min_value
    # 탐색이 완료되었다면
    if depth == len(cctv):
        count = 0 # 사각지대 개수 초기화
        # 사각지대 찾기
        for i in range(n):
            count += board[i].count(0)
        min_value = min(min_value, count)
        return 

    # 계속해서 탐색
    temp = copy.deepcopy(board) # 보드 복제
    cctv_num, x, y = cctv[depth] # 탐색할 cctv
    # cctv 방향에 따라서
    for i in mode[cctv_num]:
        fill(temp, i, x, y) # 보드, cctv방향, 좌표
        dfs(depth + 1, temp) # 재귀호출
        temp = copy.deepcopy(board) # 보드 초기화

min_value = int(1e9)
dfs(0, board) # 전체 cctv 개수가 될때까지 돌기
print(min_value)
