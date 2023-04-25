import sys
import copy
input = sys.stdin.readline
n = int(input())
array = [list(input()) for _ in range(n)]

def count(array):
    Max = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if array[i][j] == array[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)
        cnt = 1
        for j in range(1,n):
            if array[i][j] == array[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max, cnt)
    return Max

answer = 0
for i in range(n):
    for j in range(n):
        #열 바꾸기
        if j+1 < n:
            #인접한 것과 바꾸기
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
            temp = count(array)
            answer = max(answer, temp)
            #바꿨던 것을 다시 원래대로 돌려놓기
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j]

        if i+1 < n:
            #인접한 것과 바꾸기
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
            temp = count(array)
            answer = max(answer, temp)
            #바꿨던 것을 다시 원래대로 돌려놓기
            array[i][j], array[i+1][j] = array[i+1][j], array[i][j]

print(answer)