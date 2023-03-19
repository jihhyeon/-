#1. 자리수 입력받기, 왼쪽합, 오른쪽합 미리 설정해놓기
#2. 범위가 자릿수의 반 이하이면 -> left_sum에 추가
#3. 범위가 자릿수의 반 이상이면 -> right_sum에 추가
#4. left_sum 과 right_sum 비교하기
n = list(map(int, input()))
left_sum = 0
right_sum = 0

for i in range(len(n)):
    if i < (len(n)//2):
        left_sum += n[i]
    else:
        right_sum += n[i]

if left_sum == right_sum:
    print('LUCKY')

else:
    print('READY')