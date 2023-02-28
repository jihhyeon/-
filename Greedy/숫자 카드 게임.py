#먼저 행 선택 -> 가장 숫자가 낮은 카드 뽑음 -> 이때의 숫자가 가장 높은 수여야함
n, m = map(int, input().split())#행, 열
min_list = []#[1,1,2]
for i in range(n):
    data = list(map(int, input().split()))
    min_list.append(min(data))

answer = max(min_list)
print(answer)