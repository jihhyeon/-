#문자열s에 있는 모든 숫자를 전부 같게 만들기
#s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
n = list(map(int, input()))

count0 = 0 # 문자열 모두 0으로 바꾸는 경우
count1 = 0 # 문자열 모두 1로 바꾸는 경우
 
# 첫번째 원소에 대하여
if n[0] == '1':
  count0+=1
else:
  count1+=1
 
# 두번째 원소부터 마지막까지 확인
for i in range(1,len(n)-1):
  if n[i] != n[i+1]: # 현재 수와 다음수가 같지 않을 때 다음수를 현재수와 같게 바꾼다.
    # 다음 수를 0으로 바뀌는 경우
    if n[i+1] == '1':
      count0+=1
    # 다음 수를 1로 바뀌는 경우
    else:
      count1+=1
 
print(min(count0,count1))