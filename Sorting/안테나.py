#첫집과 마지막집을 제외한 가운데 있는 집들 중 정답이 있을 것임
n = int(input())
antena = list(map(int, input().split()))
antena.sort()
print(antena)
answer = []

for i in range(1, n-1):
    home = antena[i]#기준 집 = antena[1] = 5
    cnt = 0
    for j in range(n):#0,1,2,3
        if antena[j] == home and j == i:#j와 i가 인덱스도 같고 같은 값일경우
            continue
        else:
            cnt += abs(home - antena[j])#기준 - 다른 집
    answer.append([antena[i], cnt])
answer.sort(key = lambda x:(x[1], x[0]))
print(answer)
print(answer[0][0])
#----------------------------------
#답 : 정확히 중간값에 해당하는 위치의 집
print(antena[(n-1)//2])




