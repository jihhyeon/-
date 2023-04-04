import sys
input = sys.stdin.readline
w,n = map(int, input().split())
price = []
for i in range(n):
    price.append(list(map(int, input().split())))
price.sort(reverse = True, key = lambda x:x[1])#[[70,2],[90,1]]
result = 0#비용


for m, p in price:
    if w > m:
        result += m * p
        w -= m
    else:
        result += w * p
        break

print(result)
