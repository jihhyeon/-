#1. 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):#0
    idx = i#0
    print('first idx: ', idx)
    for j in range(i+1, len(array)):#1,2,...,9
        print('J', j, 'i', i)
        if array[idx] > array[j]:#7>5
            idx = j
            print('idx', idx, 'array', array[idx])
    array[i], array[idx] = array[idx], array[i]
    print(array)

print(array)

#2. 삽입 정렬
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):#3
    for j in range(i, 0, -1):#3,2,1
        print('i:', i, 'j:', array[j], 'j-1:', array[j-1])
        if array[j] < array[j-1]:#new j가 이전 j보다 작을 때
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:#new j가 이전 j보다 클때
            print('continue')
            continue
print(array)

#3. 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:#원수가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:#엇갈릴 경우
            array[right], array[left] = array[left], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        print(array)

    quick_sort(array,start, right-1)#
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)





