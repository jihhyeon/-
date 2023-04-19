"""(몸무게, 키) 둘다 커야 "큰 덩치"가 됨
돌아가며 자신보다 덩치 큰 사람의 수 = k 정하기 , 덩치 등수 = k+1
"""
n = 9
# array = [list(map(int, input().split())) for _ in range(n)]
array = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
answer = [0]*len(array)
result = 0

for i in range(len(array)):
    a, b = array[i][0], array[i][1]#55,195
    for j in range(len(array)):
        c, d = array[j][0], array[j][1]
        if a < c and b < d:
            result += 1
    print(result + 1, end = " ")
    result = 0

# print(answer)
        
