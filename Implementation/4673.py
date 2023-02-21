#d(n) = n+ n의 각자리수
#n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열
#생성자가 없는 숫자 = 셀프 넘버
#일의 자리에서는 홀수가 셀프넘버
# 10의 자리에서는 {d(n*10-1) + 2}가 셀프 넘버
# ----------------------------------------
#생성자가 있는 set을 만들고 전체 set에서 빼주기 -> 그럼 셀프 넘버 set이 나옴
#set을 사용하는 이유 : 자료형의 중복을 제거하기 위함
num = set(range(1,10000))
generated_num = set()

for i in num:
    for j in str(i):
        i += int(j)
    generated_num.add(i)#set에 원소 추가

self_num = sorted(num - generated_num)#차집합후 정렬하기
for i in self_num:
    print(i)
