import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
taller = [[] for _ in range(n+1)]
smaller = [[] for _ in range(n+1)]
# i학생 : [i보다 작은 학생 수, 큰 학생 수]
hei_dic = {i:[0,0] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    taller[a].append(b)
    smaller[b].append(a)
ans = 0

# 1.한명씩 돌면서 작은키 수 세기
def small(x):
    global visited1, smaller, s
    visited1[x] = True
    for i in smaller[x]:
        if not visited1[i]:
            s += 1
            small(i)

# 2. 한명씩 돌면서 큰키 수 세기
def tall(x):
    global visited2, taller, t
    visited2[x] = True
    for i in taller[x]:
        if not visited2[i]:
            t += 1
            tall(i)

for i in range(1,n+1):
    s, t = 0, 0
    visited1 = [False] * (n+1)
    small(i)
    visited2 = [False] * (n+1)
    tall(i)
    hei_dic[i][0], hei_dic[i][1] = s, t
    
# 3. 작은키 수 + 큰키 수 = n - 1(본인) 이면 알 수 있는 학생임
for i in range(1,n+1):
    if (hei_dic[i][0] + hei_dic[i][1]) == n - 1:
        ans += 1
print(ans)
