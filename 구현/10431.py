import sys
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    cnt=0

    for i in range(1, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                print(a[i], a[j])
                a[i], a[j] = a[j], a[i]
                cnt += 1

    print(a[0], cnt)
