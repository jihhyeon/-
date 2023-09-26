n = int(input())
ans = 0
# 행을 나타냄
row = [0]*n

# 해당 위치에 퀸을 놓을 수 있는지
def is_promising(x):
    for i in range(x):
        # 같은 열에 다른 퀸이 있는 경우, 
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

def n_queens(x):
    global ans
    if x == n:
        # 모든 퀸을 놓았음
        ans += 1
        return

    else:
        for i in range(n):
            # [x,i]에 퀸을 놓겠다
            row[x] = i
            # 퀸을 놓을 수 있으면 다음 퀸을 놓자
            if is_promising(x):
                n_queens(x + 1)
