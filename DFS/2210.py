#입력 숫자들을 str취급해주어 글자 더해가기
matrix = [list(map(str, input().split())) for _ in range(5)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = []

def dfs(x, y, number):
    if len(number) == 6:#6자리 숫자가 만들어졌다면
        if number not in result:#result에 없다면(중복되지 않다면)
            result.append(number)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, number + matrix[nx][ny])#6글자가 될때까지 재귀

for i in range(5):
    for j in range(5):
        dfs(i,j,matrix[i][j])

print(len(result))
