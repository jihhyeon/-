#점화식!!
#f(n) = f(n-1)+f(n-2)+f(n-3) , 단 n>3일 때 성립
t = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)

for i in range(t):
    n = int(input())
    print(sol(n))