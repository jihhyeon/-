#point : 최대양을 구하는 것이기 때문에 내림차순으로 정렬하고 더하기
n  = int(input())
array = list(map(int, input().split()))
array.sort(reverse = True)#내림차순
sum = array[0]
for i in range(1,len(array)):
    sum += array[i] / 2

print(sum)