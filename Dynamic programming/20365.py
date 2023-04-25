n = int(input())
array = list(map(str, input().rstrip()))
color = {'R' : 0, 'B' : 0}
color[array[0]] += 1
for i in range(1, n):
    if array[i] != array[i-1]:

        color[array[i]] += 1
#전체를 뒤집는것 하나 추가!(+1)
print(min(color['R'], color['B'])+1)

