# from collections import deque
# n, x = map(int, input().split())
# num = list(map(int, input().split()))
# # que = deque(num)
# cnt = 0
# start, end = 0, len(num)-1
# while start <= end:
#     mid = (start+end)//2
#     print(start, end)
#     print('mid', mid, 'cnt', cnt)
#     if num[mid] == x:
#         cnt += 1
#         num.pop(mid)
#     elif num[mid] < x:
#         start = mid + 1
#     else:
#         end = mid -1

# if cnt == 0:
#     print(-1)
# else:
#     print(cnt)
#--------------------------
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
num = list(map(int, input().split()))

count = count_by_range(num, x, x)

if count == 0:
    print(-1)
else:
    print(count)



