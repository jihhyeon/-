#시뮬레이션 문제
#기둥 : 바닥위, 보의 한쪽 끝부분위, 다른 기둥 위
#보 : 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결될ㄷ
#(기둥, 보)인 경우와 (설치, 삭제)인 경우로 나눠서 보기
def solution(n, build_frame):
    answer = []
    
    def possible(answer):
        for x, y, stuff in answer:
            if stuff == 0:
                if y == 0 or [x-1,y,1] in answer or [x,y,1]in answer or [x,y-1,0] in answer:
                    continue
                return False#아니면 거짓 반환
            elif stuff == 1:
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                    continue
                return False    
        return True
           
    for frame in build_frame:
        x, y, stuff, operate = frame
        #삭제하는 경우
        if operate == 0:
            answer.remove([x,y,stuff])#일단 삭제해봄
            if not possible(answer):#possble이 거짓으로 나왔을 때
                answer.append([x,y,stuff])#설치
        #설치하는 경우
        if operate == 1:
            answer.append([x,y,stuff])#일단 설치해봄
            if not possible(answer):#possible이 거짓으로 나왔을 때
                answer.remove([x,y,stuff])#삭제
    return sorted(answer)