#여기서의 큰수 법칙 : 다양한 수로 이루어진 배열 -> 주어진 수들을 M번 더해 가장 큰수 만들기
#단, 배열의 특정 인덱스에 해당하는 수 -> 연속 k번 초과해 더해질 수 없음
#단, 서로 다른 인덱스에 해당하는 숫자가 같은 경우에도 서로 다른 것으로 간주
n, m, k = map(int, input().split())
give = [2,4,5,4,6]
give_1 = [3,4,3,4,3]
#1. 가장 큰 값을 가진 인덱스 추출 -> 여러개 일수도 있으니 for문으로 확인
#2. k값으로 for문 돌려서 계산, -> 인덱스가 하나일 경우 -> k번+두번째로 큰값+k번
# 3.       -> 인덱스가 두개 경우 -> m번 계속 돌려도 될듯 
cnt = 0
answer = 0
idx_list = []
give.sort(reverse = True)
give_set = list(set(give))
give_set.sort(reverse = True)

first = give_set[0]#최댓값
sec = give_set[1]#두번째로 큰 값


for idx, i in enumerate(give):
    if i == first:
        cnt += 1
        idx_list.append(idx)

if cnt == 1:
    #몫만큼 최댓값 더하고, 나머지만큼 둘째값 더하기
    answer = int(first) * k * (m // k)
    answer += int(sec) * (m % k)
elif cnt > 1:
    answer = int(first) * m

print(answer)