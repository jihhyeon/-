import sys
input = sys.stdin.readline

def choice(idx, sum):
    global max_sum
    if idx == 11:
        if sum > max_sum:
            max_sum = sum
        return

    for i in range(11):
        if line[idx][i] != 0 and visit[i] == 0:
            visit[i] = 1
            choice(idx+1, sum+line[idx][i])
            # print('idx:', idx, '능력치:', line[idx][i])
            visit[i] = 0

n = int(input())
for tc in range(n):
    line = []
    for _ in range(11):
        line.append(list(map(int, input().split())))
    visit = [0]*11
    max_sum = 0
    choice(0,0)
    print(max_sum)

