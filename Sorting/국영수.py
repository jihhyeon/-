#입력
n = int(input())
student = []
for i in range(n):
    li = list(input().split())
    student.append(li)
print(student)
student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))#내림차순은 '-'붙이면 됨

for i in range(n):
    print(student[i][0])

    