import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int,input().split())) for _ in range(m)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
rain = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]
around = 0

while True:
    if around == m:
        break

    # 1. 구름 방향으로 이동
    d, s = ds[around][0] - 1, ds[around][1]

    for ra in rain:
        ra[0] = abs(ra[0] + dx[d] * s) % n
        ra[1] = abs(ra[1] + dy[d] * s) % n
    print('first',rain)

    # 2. 각 구름에서 비 내려 물의 양 1 증가
    visited = [[False] * n for _ in range(n)] # 구름있는 위치 표시
    for ras in rain:
        x, y = ras[0], ras[1]
        arr[x][y] += 1
        visited[x][y] = True # 구름 위치 표시하기
    # print(*arr, sep = '\n')

    # 3. 대각선 방향 바구니수만큼 물의 양 증가시키기
    for rass in rain:
        cnt = 0 # 바구니개수
        for i in range(1,9,2):
            nx = rass[0] + dx[i]
            ny = rass[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0:
                cnt += 1
        arr[rass[0]][rass[1]] += cnt
    # print(*arr, sep = '\n')

    rain = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                rain.append([i,j])
    print('rain')
    print(rain)

    around += 1
            




