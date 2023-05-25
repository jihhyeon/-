import sys
input = sys.stdin.readline
l,c = map(int, input().split())#암호글자수, 주어지는 원소 개수
array = sorted(list(map(str, input().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []

def back_tracking(cnt, idx):
    #암호를 만들었을 때
    if cnt == 1:
        vo,co = 0,0

        for i in range(l):
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1
        print(answer)
        if vo >= 1 and co >= 2:
            print("".join(answer))
        return
    #반복문을 통해 암호 만들기
    for i in range(idx, c):#0,6
        answer.append(array[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()

back_tracking(0,0)

