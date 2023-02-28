
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:#배수
        if n % m == 0:
            print("multiple")
        else:
            print("neither")
    elif n < m:#약수 , m이 n의 약수
        if m % n == 0:
            print("factor")
        else:
            print("neither")
