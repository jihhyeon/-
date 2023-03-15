#선생님 = T, 학생 = s, 장애물 = o
#선생님t의 상하좌우에 학생s이 있다면 no
#상하좌우가 x가 아니면 장애물 설치
#장애물은 정확히 3개 설치해야함
#벽을 설치할 수 있는 모든 경우를 찾는 함수 / 선생의 위치에서 상하좌우로 학생이 있는지 확인하는 함수
n = int(input())
graph = []
teacher = 0
for _ in range(n):
    data = list(map(str, input().split()))
    teacher += data.count('t')
    graph.append(data)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def check_s(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<=nx<n and 0<=ny<n and graph[nx][ny] != 'o':
            #감시 가능하다
            if graph[nx][ny] == 's':
                return True
            else:
                #t나 x였으면 계속 탐색
                nx += dx[i]
                ny += dy[i]
    return False

def solution(count):
    global answer
    if count == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 't':
                    if not check_s(i, j):
                        cnt += 1
        if cnt == teacher:
            answer = True
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'x':
                graph[i][j] = 'o'
                count += 1
                solution(count)
                graph[i][j] = 'x'
                count -= 1
answer = False
solution(0)
if answer:
    print('yes')
else:
    print('no')