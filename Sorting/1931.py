n = int(input())#회의의 수
#1. 순서대로 입력 받는 graph 만들기
#2. 그래프 첫줄부터 회의수 count하기
#2-1. 어떻게 count? 해당 시간보다 앞시간 존재하고+끝나는 시간도 해당시간 보다 앞이면 cnt+1
#2-2. 같거나 뒷시간 존재하면 cnt +1
graph = [[0]*2 for _ in range(n)]
cnt = 0#최종 회의 개수
#첫째 줄 리스트 = li
def down(li, cnt):
    for i in graph:
        if (i[1] <= li[0]) & (i[0] != li[0]):#끝시간이 같거나 작다면, 단 i와 li는 같으면 안됨
            cnt += 1
            down
    return cnt

def up(li, cnt):
    for i in graph:
        if (i[0] >= li[1]) & (i[0] != li[0]):#앞시간이 같거나 크다면, 단 li와 같으면 안됨
            cnt += 1
        else:
            break


