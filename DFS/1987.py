
r,c = map(int, input().split())
array = [list(map(str, input().rstrip())) for _ in range(r)]
visited = set()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    visited.add(array[x][y])
    print('add', visited)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0<=nx<r and 0<=ny<c:
            if array[nx][ny] not in visited:
                print('yes dfs', array[nx][ny])
                dfs(nx, ny, cnt + 1)
    visited.remove(array[x][y])
    print('remove', visited)

dfs(0,0,1)

print(ans)

    
    




