# #1. 문자열 반복
n = int(input())
answer = []
for i in range(n):
    m, n = list(map(str, input().split()))
    for j in n:
        print(j*int(m), end='')#m만큼 곱해주고, 공백 없애기
    print()

#2. 단어공부
#대소문자 구분없음 -> 모든 입력값을 소문자로 변환하기
string = list(input().lower())
string_list = list(set(string))#중복없는 리스트

cnt_list = []
for i in string_list:
    cnt = string.count(i)#i의 개수 반환
    cnt_list.append(cnt)
print(cnt_list)#[1, 4, 4, 1]
if cnt_list.count(max(cnt_list)) > 1:#최댓값의 개수가 1초과 = 최댓값이 중복된다면
    print("?")
else:
    max_cnt = cnt_list.index(max(cnt_list))#cnt_list의 인덱스 = 
    string_cnt = string_list[max_cnt]#string list인덱스
    print(max_cnt, string_cnt)
    print(string_cnt.upper())




