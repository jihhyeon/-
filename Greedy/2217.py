n = int(input())
array = []
result = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse = True)

for i in range(1,n+1):
    result.append(array[i-1]*i)
print(max(result))