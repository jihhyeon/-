n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
#오름차순 정렬하기
n_list.sort()
m_list.sort()

def binary_search(n_list, target, start, end):#array, target, start, end
    while start <= end:
        #중간점 인덱스 설정
        mid = (start+end)//2
        if n_list[mid] == target:
            return "yes"
        elif n_list[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return "no"



for i in m_list:
    start = 0
    end = i-1
    print(binary_search(n_list, i, start, end), end = ' ')