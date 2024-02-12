from collections import deque
import sys
input = sys.stdin.readline

arr = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
rot = [list(map(int, input().split())) for _ in range(k)]
around = 0
ans = 0

def check(idx, dirr):
    global diff, arr, visited
    visited[idx] = True
    arr[idx].rotate(dirr) # 회전하기

    for j in diff[idx]: # 3,1
        print('j',j)
        if j and not visited[j]:
            if dirr == 1:
                arr[j].rotate(-1)
            else:
                arr[j].rotate(1)
        print('rot',arr)


# 2. 회전하기
for idx, direction in rot:
    idx -= 1

    # 1. 극이 다른지 확인하기
    diff = [[] for _ in range(4)]
    for i in range(3):
        if arr[i][2] != arr[i+1][6]:
            diff[i].append(i+1)
            diff[i+1].append(i)
    print('diff',diff)

    visited = [False] * (4)
    print('idx',idx, 'dir',direction)
    check(idx, direction)
print(arr)

# 3. 출력하기
if arr[0][0] == 1:
    ans += 1
if arr[1][0] == 1:
    ans += 2
if arr[2][0] == 1:
    ans += 4
if arr[3][0] == 1:
    ans += 8

print(ans)

