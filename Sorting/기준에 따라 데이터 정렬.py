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

# print(array)