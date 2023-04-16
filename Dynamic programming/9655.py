# n = int(input())
# dp = [False] * (n)
# dp[0] = n#남는 돌의 개수


# for i in range(1, n):
#     # print(i)
#     if n == 0:
#         break
#     if dp[i-1] > 3:
#         dp[i] = dp[i-1] -3
#         n -= dp[i-1]-3
#     if dp[i-1] < 3 and dp[i-1] >= 1:
#         dp[i] = dp[i-1]-1
#         n -= dp[i-1]-3
# idx = dp.index(0)
# if idx % 2 == 0:
#     print('CY')
# else:
#     print('SK')
'''규칙 ...! : n이 홀수일 때, 짝수일 때에 따라 승패가 결정됨..'''
n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')


