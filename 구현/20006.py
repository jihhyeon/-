p, m = map(int, input().split())
array = []
for _ in range(p):
    l,n = map(str,input().split())
    array.append([int(l),n])#레벨, 닉네임 저장하기
cnt = p
room = []

for l,n in array:
    flag = False
    for i in range(len(room)):
        if len(room[i][1]) == m:
            continue

        #들어갈 수 있는 방이 있으면 입장
        if room[i][0] - 10 <= l <= room[i][0] + 10:
            flag = True
            room[i][1].append([l,n])#방 리스트
            break

    #대기방에 들어갈 수 없으면 새로운 방 생성
    if not flag:
        room.append([l,[[l,n]]])

#방이 생성된 시간 순서로 출력
for i in range(len(room)):
    if len(room[i][1]) == m:
        print('Started!')
        tmp_ids = sorted(room[i][1], key = lambda x:x[1])
        for j in range(m):
            print(*tmp_ids[j])
    else:
        print('Wating!')
        tmp_ids = sorted(room[i][1], key = lambda x:x[1])
        for j in range(len(tmp_ids)):
            print(*tmp_ids[j])

print(room)
