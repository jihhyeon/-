n, k = map(int, input().split())
array = [i for i in range(1, n+1)]
ans = []
num = 0
for i in range(n):
    num += (k-1)
    if num >= len(array):
        print(num, len(array))
        num %= len(array)
        print(num)
    ans.append(str(array[num]))
    array.pop(num)
print("<",', '.join(ans),">", sep = "")