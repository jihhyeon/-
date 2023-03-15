#상하좌우로 이동 단, 범위밖은 무시하기
n = int(input())
move_li = list(map(str, input().split()))#R R R U D D
move = ['L','R', 'U', 'D']#왼,오,위,아래
dx = [-1,1,0,0]
dy = [0,0,-1,1]
x, y = 0, 0
for i in move_li:
    for j in range(len(move)):
        if i == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<n and 0<=ny<n:
                x, y = nx, ny
                print(x,y)

print(y+1, x+1)
