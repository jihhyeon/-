import sys
import heapq
input = sys.stdin.readline

n,h,t = map(int, input().split())
count = 0

heap = []
for _ in range(n):
    heapq.heappush(heap, -int(input()))
print(heap)

for i in range(t):
    a = heapq.heappop(heap)#음수에서 가장 작은 것 = 절댓값씌우면 가장 큰수
    print('a',a)
    if abs(a) < h:
        heapq.heappush(heap,a)
        break
    elif abs(a) == 1:
        heapq.heappush(heap,a)
    else:
        a = -(abs(a)//2)
        heapq.heappush(heap,a)
        count += 1
if abs(min(heap)) < h:
    print('YES')
    print(count)

else:
    print('NO')
    print(abs(heapq.heappop(heap)))

"""
n, h, t = map(int, input().split())
stop_t = t
arr = []
ans = [False]*n
for _ in range(n):
    arr.append(int(input()))

while True:
    if t == 0:
        break
    for i in range(stop_t):
        print(i%stop_t)
        if arr[i%stop_t] == 1:
            continue
        else:
            arr[i%stop_t] = int(arr[i%stop_t]/2)
            t -= 1
            print(arr)

for i,num in enumerate(arr):
    if num < h:
        ans[i] = True
    else:
        ans[i] = False

if False in ans:
    print(max(arr))
else:
    print(arr)"""