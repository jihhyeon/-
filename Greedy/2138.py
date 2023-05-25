"""첫번째 스위치를 누르는 경우와 누르지 않는 경우로 분리"""
n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

def change(A,B):
    L = A[:]
    press = 0
    for i in range(1,n):
        #이전 전구가 같은 상태면 pass
        if L[i-1] == B[i-1]:
            continue
        press += 1
        for j in range(i-1, i+2):#i-1, i, i+1
            if j<n:#n범위 안에 있다면
                L[j] = 1 - L[j]#상태 바꿔주기
    if L == B:
        return press
    else:
        return 1e9

#첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
#첫번째 전구의 스위치를 누르는 경우(상태 바꿔주고 시작)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb,target) + 1)#두경우 비교하여 min값 도출

print(res if res != 1e9 else -1)