#n에서 1을 뺀다 / n을 k로 나눈다
#N이 1이 될때까지 1,2번과정을 수행해야하는 최소 횟수 구하기
#--------------------------------내 코드
"""n, k = map(int, input().split())
answer = 0
while n>1:
    if n % k == 0:
        answer += 1
        n = int(n//k)#5
    else:
        n -= 1
        answer += 1
print(answer)"""

#-------------------------------책 코드
n, k = map(int, input().split())
result = 0

while True:
    #n이 k보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #n이 k로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n//k)*k#n과 가장 가까운 k의 배수
    result += (n-target)#n에서 target까지 되도록 -1해야하는 횟수 더함
    n = target#한번에 빼주기
    print('target:', target, 'result:', result,'n:',n)
    #n을 k로 나눠주고 result +1해주기
    n //= k
    result += 1
    print('result:', result,'n:',n)
#마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)

print(result)