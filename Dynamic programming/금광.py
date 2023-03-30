"""from collections import deque
t = 2
n, m = 4,4
graph = [[1,3,1,5],
[2,2,4,1],
[5,0,2,3],
[0,6,1,2]]
visited = [[0]*m for _ in range(n)]

dx = [-1,0,1]
dy = [1,1,1]
big = []
for i in range(n):
    big.append(graph[i][0])
start = big.index(max(big))
print(start)

que = deque()
que.append([start,0])
count = graph[start][0]
print(count)
while que and n<=4:
    result = []#세 방향에 대한 최댓값을 구하려는 리스트
    result_idx = []
    a, b = que.popleft()
    print(a,b)
    if a == n and b == m:
        break
    for i in range(3):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            result.append(graph[nx][ny])
            result_idx.append([nx,ny])
            print('result', result)
            print('result_idx', result_idx)
    if result:
         max_num = max(result)
         count += max_num
         que.append(result_idx[result.index(max(result))])
         print('max_num, count',max_num, count)
print(count)"""
#----------------------------------
for tc in range(int, input()):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)



        
