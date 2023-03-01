n = int(input())
answer_li = []
for i in range(n):
    data = int(input())
    answer_li.append(data)#answer_li.append(int(input()))

answer_li.sort(reverse = True)#array = sorted(array, reverse = True)

for j in answer_li:
    print(j, end = ' ')#공백으로 구분하여 출력