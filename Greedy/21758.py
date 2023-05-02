#직관적으로 벌이 최대한 꿀로부터 멀리 떨어져있어야 꿀의 양도 최대가 될것
n = int(input())
ans = 0
honey_place = list(map(int,input().split()))
prefix_sum = []
prefix_sum.append(honey_place[0])
#꿀 합에 대한 누적합
for i in range(1, n):
  prefix_sum.append(prefix_sum[i-1] + honey_place[i])

# 꿀통이 왼쪽 끝
for i in range(1, n-1):
  ans = max(ans,prefix_sum[n-2] + prefix_sum[i-1] - honey_place[i])

# 꿀통이 오른쪽 끝
for i in range(1, n-1):
  ans = max(ans, prefix_sum[n-1] - honey_place[0] + prefix_sum[n-1] - prefix_sum[i] - honey_place[i])
  
# 꿀통 가운데
for i in range(1, n-1):
  ans = max(ans,prefix_sum[n-2] - honey_place[0] + honey_place[i])
print(ans)