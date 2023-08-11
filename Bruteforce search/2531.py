# from collections import deque
import sys
input = sys.stdin.readline
n,d,k,c = map(int, input().split())
rotate_list = []
for i in range(n):
    rotate_list.append(int(input()))

su_list = []
ans = 0

for i in range(n):
    li = rotate_list[0:k]
    num_su = len(set(li))
    if num_su == k:
        su_list.append(li)
    rotate_list.append(rotate_list[0])
    rotate_list.remove(rotate_list[0])

for su in su_list:
    su.append(c)
    su_num = len(set(su))
    ans = max(ans, su_num)

print(ans)
    
