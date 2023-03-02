#모든 숫자를 확이낳며 숫자사이에 곱셈, 덧셈 연산자를 넣어 가장 큰수를 구하는 프로그램 작성
#모든 연산은 왼쪽에서부터 순서대로 이루어짐
#0, 1이있으면 그 다음 숫자와 무조건 더하기, 최댓값을 만드는 것은 곱셈으로!
import time
n = list(map(int, input()))
# answer = 0

# start_time = time.time()
# if (int(n[0]) == 0) or (int(n[0]) == 1):#첫수가 0, 1일때
#     answer += int(n[1])
# else:
#     answer = int(n[0])*int(n[1])

# for i in range(1, len(n)-1):
#     if (int(n[i]) == 0) or (int(n[i]) == 1):
#         answer += int(n[i+1])

#     else:
#         answer *= int(n[i+1])

# end_time = time.time()
# print(answer)
# print('time:', end_time - start_time)#0.00023126602172851562

result = n[0]#첫번째 정수를 초기 결과값으로 지정
start_time = time.time()
for i in range(1, len(n)):
    if n[i] <= 1 or result <= 1:#해당 정수가 1 이하거나, 초기 결과값이 1 이하일 경우
        result += n[i]
    else:
        result *= n[i]
end_time = time.time()
print('time:', end_time - start_time)# 0.00014519691467285156
print(result)
