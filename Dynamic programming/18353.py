"""병사 배치시 : 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
특정 위치에 있는 병사 열외시킴 + 남아있는 병사의 수가 최대가 되도록
dp[i-1]>dp[i]
1. 리스트를 돌며 이전의 값보다 큰값이 존재할 때
2. 해당 값을 dp 테이블에 추가하지 않고 cnt += 1하기(열외시킨 병사 수)
"""
n = int(input())
array = [15,11,4,8,5,2,4]
# cnt = 0
# dp = []
# for i in range(len(array)):
#     print(dp)
#     if i != len(array)-1:
#         print(i)
#         print(array[i], array[i+1])
#         if array[i] >= array[i+1]:
#             dp.append(array[i])
#         elif array[i] < array[i+1]:
#             cnt += 1
#             print(cnt)
#     else:
#         if dp[-1] >= array[6]:
#             dp.append(array[len(array)-1])
#         else:
#             cnt += 1

# print(dp, cnt)
"""가장 긴 증가하는 부분 수열 : 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
D[i] = max(D[i], D[j]+1) if array[j]<array[i]
"""
array.reverse()#정렬 뒤집기

dp = [1]*n
#가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):#1
    for j in range(0,i):#0
        print(i,j)
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))