#그냥 리스트 자체를 비교해도 되었던 문제지만!
#나는 이렇게 풀었다
import sys
array = list(map(int, input().split()))

def asc_search(st_idx, end_idx, array):
    for i in range(st_idx, end_idx):
        if i != array[i-1]:
            return print('mixed')
    return print('ascending')

def des_search(st_idx, end_idx, array):
    for i in range(st_idx, end_idx,-1):#8,7,6,5,4,3,2,1
        if i != array[abs(st_idx-i)]:
            return print('mixed')
    return print('descending')

if array[0] == 1:
    asc_search(1,len(array)+1,array)
elif array[0] == 8:
    des_search(len(array),0,array)
else:
    print('mixed')


