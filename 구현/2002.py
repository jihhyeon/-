n = int(input())
dj = [str(input()) for _ in range(n)]
ys = [str(input()) for _ in range(n)]
ans = 0

dj_dict = {}
for key, val in enumerate(dj):
    dj_dict[val] = key + 1

ys_dict = {}
for key, val in enumerate(ys):
    ys_dict[val] = key + 1

#인덱스가 대근 < 영식 이면 추월한 것
for key_dj, val_dj in dj_dict.items():
    if ys_dict[key_dj] < val_dj:
        print('in', key_dj, 'out', key)
        ans += 1

print(ans)