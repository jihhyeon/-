import sys
input = sys.stdin.readline

t = int(input())
#test case start
for i in range(t):
    n = int(input())
    emplo = []
    for j in range(n):
        emplo.append(list(map(int, input().split())))
    #서류등수로 정렬
    emplo.sort(key = lambda x:x[0])

    l = emplo[0][1]
    ans = 1
    for j in range(1,n):
        if emplo[j][1] < l:
            l = emplo[j][1]
            ans += 1
    print(ans)



