#1. 구구단
n = int(input())
for i in range(1,10):
    print(n,"*", i, "=", n*i)

#2. A+B -5
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(n+m)