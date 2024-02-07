import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]

milks = [] # 우유의 위치를 저장할 리스트
hx, hy = 0,0 # 집의 위치
ans = 0

# 2. dfs
def dfs(jwx, jwy, hp, milk):
    global ans
    print('dfs', jwx, jwy)

    for x, y in milks:
        if village[x][y] == 2: # 현재까지 마시지 않은 우유인가
            dist = abs(jwx - x) + abs(jwy - y) # 지금 위치와 우유사이 거리
            if dist <= hp:# 현재 체력으로 도달할 수 있는 위치인가
                village[x][y] = 0 # 보드위에 이번 우유를 마셨다고 표시
                print(x, y)
                print('거리', dist, '체력', hp)
                dfs(x,y, hp + h - dist, milk + 1)
                village[x][y] = 2 # 다시 복구
                print('복구', x,y)

    # 집과 현재거리가 체력보다 작으면 ans와 비교하여 큰값 설정            
    if abs(jwx - hx) + abs(jwy - hy) <= hp:
        ans = max(ans, milk)
        print('정답', ans)

# 1. 우유의 위치와 집의 위치 저장
for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            hx, hy = i,j
        if village[i][j] == 2:
            milks.append([i,j])

print('처음', hx, hy)
dfs(hx, hy, m, 0)
print(ans)