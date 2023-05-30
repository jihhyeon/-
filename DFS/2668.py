"""import sys
input = sys.stdin.readline
n = int(input())
array = [0]#[0, 3, 1, 1, 5, 5, 4, 6]
ans = []
for i in range(1, n+1):
    a = int(input())
    array.append(a)

def dfs(idx, val):
    for i in range(idx+1, n + 1):
        # print(i, array[i], idx, val)
        if i == val and array[i] == idx:
            # print('before:', idx, val, 'after:', i, array[i])
            ans.append(i)
            ans.append(array[i])

for i in range(1, n+1):
    #인덱스와 값이 같을 떄
    if i == array[i]:
        ans.append(i)
    dfs(i,array[i])

print(len(ans))
ans.sort()
print(*ans, sep = '\n')"""

import sys
input = sys.stdin.readline
def dfs(v, i):
    visited[v] = True
    w = data[v]
    if not visited[w]:
        dfs(w, i)
    elif visited[w] and w == i:
        result.append(w)
n = int(input())
data = [0] + [int(input()) for _ in range(n)]
result = []
for i in range(1, n + 1):
    visited = [False]*(n+1)
    dfs(i,i)
print(len(result))
result.sort()
for i in result:
    print(i)