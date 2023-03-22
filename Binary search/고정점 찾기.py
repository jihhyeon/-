n = int(input())
array = list(map(int, input().split()))
start, end = 0, len(array)-1
answer = 0

def binary_search(array, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

idx = binary_search(array, start, end)
if idx == None:
    print(-1)
else:
    print(idx)