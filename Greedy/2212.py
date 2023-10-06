import sys 

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
dist = []
# 집중국 개수가 센서 개수보다 크거나 같으면 집중국을 센서 위치에 설치하면 되므로 = 0
if k >= n:
    print(0)
    sys.exit()

for i in range(1,n):
    dist.append(sensor[i]-sensor[i-1])

dist.sort(reverse = True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))

