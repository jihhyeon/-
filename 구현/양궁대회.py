n, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x:x[0])

print(array)

# for i in range(n):
#     while 