#한번 사용한 객실 -> 퇴실기준으로 10분간 청소 -> 다음 손님 사용
#필요한 최소 객실수 return
#앞(퇴실시간 + 10분)과 뒤(입실시간)이 같거나 이후시간이면 같은방, 다르거나 이전시간이면
#다르거나 이전시간인경우 : 앞(입실시간)이 뒤(퇴실시간+10)보다 뒤이면 같은 방
#윗 경우 아니면 다른 방
from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda _:_[0])#입실시각 기준으로 명단 정렬
    for book in book_time:
        check_in = num(book[0])
        check_out = num(book[1])+10
        if len(rooms)!=0 and rooms[0]<=check_in:#앞의 체크인시간이 현재 체크인시간보다 앞일 경우
            heappop(rooms)#rooms에서 가장 작은 원소를 pop&return
        heappush(rooms, check_out)#rooms에 check_out 추가
    return len(rooms)
def num(HHMM):
    return 60*int(HHMM[:2]) + int(HHMM[3:])
            
        
