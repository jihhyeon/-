import sys
input = sys.stdin.readline

n = int(input())
calendar = [0 for _ in range(367)]

for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        calendar[i] += 1

row = 0#높이
col = 0#너비
answer = 0

for i in range(1, 367):
    #현재 칸이 채워져있으면
    if calendar[i] != 0:
        row = max(row, calendar[i])
        col += 1
    else:
        answer += row * col
        row, col = 0,0
print(answer)
    

