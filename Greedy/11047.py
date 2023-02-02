# 첫번째 시도
'''n, k = map(int, input().split()) #동전 개수, 합
kind = list(map(int, input().split())) #동전 종류
cnt = 0

while k != 0:#k가 0이 될때 까지 반복하기
    li = []
    for i in kind:
        b = k-i #k와 동전의 차
        if b >= 0:
            li.append(b)
    k = li[-1]#차이가 제일 적은 값을 k로 할당
    # print('횟수: ', cnt, 'k값: ', k)
    cnt += 1
print(cnt)'''

#두번째 시도 -> 제일 큰 값으로 나눠주고 최소한의 동전개수 찾기
n, k = map(int, input().split())
kind = list(map(int, input().split()))
kind.sort(reverse = True)#큰값부터 역순으로 정렬
print(kind)
cnt = 0

for i in kind:
    if k == 0:
        break
    cnt += k//i #몫이 개수
    k %= i#나머지는 k값으로!
print(cnt)