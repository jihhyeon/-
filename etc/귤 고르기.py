"""서로 다른 종류를 최소로 하기
k : 한 상자에 담으려는 귤의 개수
tangerine : 귤의 크기를 담은 배열
같은 크기끼리 묶고 개수 세기(종류안에 개수 많은 귤 순으로 정렬)-> 
k개보다 작을 경우, 다른 묶음
k개보다 클 경우 1return
dict형태로 만들어도될듯 {크기:개수}
"""
def solution(k, tangerine):
    answer = 0
    #정렬하기/12233455
    sort_tan = sorted(tangerine)
    so_set_tan = list(set(sort_tan))#중복값 제거 1 2 3 4 5
    #딕셔너리 만들기/ {1:1, 2:2,3:2,4:1, 5:2}
    dict = {}
    for i in so_set_tan:
        dict[i] = 0
    for i in sort_tan:
        dict[i] += 1
        
    value_li = []
    for key, value in dict.items():
        value_li.append(value)
    value_sort = sorted(value_li, reverse = True)#[2,2,2,1,1]
    cnt = 0
    cnt_num = 0
    for val in value_sort:
        cnt += val#k개와 같아져야함/ 2+2+2
        cnt_num += 1#종류 개수 / 1+1+1
        # print("cnt", cnt)
        # print("cnt_num", cnt_num)
        if cnt >= k:
            break
        else:
            continue
    return cnt_num