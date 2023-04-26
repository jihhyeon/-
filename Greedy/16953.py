#1을 빼는 것!
st, end = map(int, input().split())
cnt = 1

while end != st:#end와 st가 같지않다면 -> 계속 연산 진행하기
    cnt += 1
    if end == st:
        break
    tmp = end

    if end % 10 == 1:
        end //= 10

    elif end % 2 == 0:
        end //= 2

    if tmp == end:
        cnt = -1
        break

print(cnt)

"""while True:
    if end <= st:
        break
    if end[-1] == str(1):
        end = end[:-1]
        cnt += 1
        print('-1', end)
    else:
        end = int(end) // 2
        cnt += 1
        end = str(end)
        print('//2', end)

if end == st:
    print(cnt+1)
else:
    print(-1)"""



