import sys
# input = sys.stdin.readline()

n = int(input())
arr = [list(input()) for _ in range(n)]
dx, dy = [-1,1,0,0,-1,-1,1,1], [0,0,-1,1,-1,1,-1,1]
res = 0 # 최대 지뢰개수

def find(x,y):
    min_bomb, near = 1e9, []# 인접지뢰값들 중 최소값, 칸의 리스트
    # 인접한 곳 돌며 min_bomb 최소값으로 지정
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '#' and arr[nx][ny] != '*' and arr[nx][ny] != '-':
            min_bomb = min(min_bomb, int(arr[nx][ny]))
            near.append([nx, ny])

    # 최소값이 1 이상인 경우, (x,y)는 지뢰 있는 것
    if min_bomb >= 1:
        arr[x][y] = '*'
        # 지뢰 있을 시, near칸 돌면서 -1씩 해주기
        for i in near:
            arr[i[0]][i[1]] = int(arr[i[0]][i[1]]) - 1

    # 최소값이 0인 경우, 지뢰 없는 것
    if min_bomb == 0:
        arr[x][y] = '-'
    # print(*arr, sep = '\n')
    
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            find(i,j)

for i in range(n):
    for j in range(n):
        if arr[i][j] == '*':
            res += 1

print(res)
