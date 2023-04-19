n = int(input())
array = list(map(int, input().split()))
m = int(input())
student = []
for _ in range(m):
    a, b = map(int, input().split())
    student.append([a,b])

def male(i, array):
    for j in range(len(array)):
        if j >= i and j % i == 0:
            array[j-1] = abs(array[j-1]-1)# 0 -> 1, 1 -> 0
    return array

def female(i, array):#i = 3
    #일단 바로 양옆이 대칭이어야함
    i = i - 1
    for j in range(len(array)):
        if 0<=i+j+1<=len(array) and 0<=i-j-1<=len(array):
            if (j == 0) and array[i-j-1] != array[i+j+1]:
                array[i-1] = abs(array[i-1]-1)
                break
            else:
                array[i-j-1] = abs(array[i-j-1]-1)
                array[i+j+1] = abs(array[i+j+1]-1)
    array[i] = abs(array[i]-1)
    return array

for i in range(len(student)):
    if student[i][0] == 1:#남학생인 경우
        male(student[i][1], array)
    if student[i][0] == 2:
        female(student[i][1], array)

for i in array:
    print(i, end = " ")


