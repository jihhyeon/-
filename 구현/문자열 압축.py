#1~s개까지 돌아가며 완전탐색하기
def solution(s):
    answer = 0
    result = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)+1):
        #1개씩, 두개씩...
        b = ''
        cnt = 1#갯수 체크
        tmp = s[:i]#i개씩 자르기
        for j in range(i, len(s)+i, i):#i부터 끝까지 i단위로 나눠 탐색
            if tmp == s[j:i+j]:#앞과 같다면
                cnt += 1
            else:
                if cnt!=1:#앞에서 중복이 있다면
                    b = b + str(cnt) + tmp
                    print(s[j:j+i])
                    print(b)
                else:#앞에서 중복이 없다면
                    b = b + tmp
                    print('else', b)
                    
                tmp = s[j:j+i]
                cnt = 1
                
        result.append(len(b))
        
    return min(result)