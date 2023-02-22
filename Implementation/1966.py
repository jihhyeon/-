#첫줄 : 문서의 개수N, 몇번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번째에 놓여있는지 M
#M은 0부터 시작
#두번째 줄 : N개 문서의 중요도가 차례로 주어짐(1이상 9이하)
#몇번째로 인쇄되는지 출력하기

# 맨 첫째줄 만큼 반복하기
#imp[m]에 해당하는 값 = m의 중요도
#중요도를 sort하여 해당
case_num = int(input())
final_num = []
for i in range(case_num):
    n, m = map(int, input().split())
    n_li = list(range(n))#리스트로 만들어주기
    imp = list(map(int, input().split()))#중요도

    if n == 1:
        final_num.append(n)
    else:
        seq = n_li[m]
        imp_seq = imp[m]
        sort_imp = sorted(imp, reverse = True)#중요도 내림차순 정렬
        idx = sort_imp.index(imp_seq)
        fin_idx = idx+1
        print(final_num)
        final_num.append(fin_idx)
# ------------
# 내림차순 정렬하면 인덱스에 대한 순서가 되지 않음
# pop을 이용하여 
test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    imp = list(map(int, input().split( )))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break#반복 중단
            #첫번째 조건 충족하는데 두번째 충족 안할 시에
            else:
                imp.pop(0)#리스트의 0번째 요소 리턴후 삭제
                idx.pop(0)
                print(imp, idx)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))    
            print(imp, idx)