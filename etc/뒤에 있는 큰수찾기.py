"""뒷 큰수 : 배열의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중 자신보다 크면서 가장 가까이있는 수
#모든 원소에 대한 뒷큰수들을 차례로 담은 배열 return
#단, 뒷큰수가 존재하지 않는 원소는 -1 return"""
def solution(numbers):
    # que = deque(numbers)
    answer = []
    for idx, num in enumerate(numbers):
        a = num#2
        sli_a = numbers[(idx+1):]#3,3,5
        if len(sli_a)>1:
            
          #a보다 큰값이 있는 경우만 돌리기
            if a<max(sli_a):
                for i in range(0, len(sli_a)):#1,5,3,6,2
                    if a<sli_a[i]:
                        answer.append(sli_a[i])
                      # numbers.pop(0)
                        break
            else:
                answer.append(-1)
              # numbers.pop(0)
              # break
        if len(sli_a)==1 or len(sli_a)==0:
            answer.append(-1)
          
    return answer