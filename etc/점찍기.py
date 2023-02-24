"""
원점과 거리가 d를 넘는 위치에는 점을 찍지 않음(사선거리포함)
k=2, d=4; x=2a->x가 4이하>x=0,2,4/ y=2b>y가 4이하>y=0,2,4
x와 y에 대한 반복문
k=1, d=5; x=a-> x=0,1,2,3,4,5/ y=b-> y=0,1,2,3,4,5
d = sqrt(x^2+y^2)
1. x축 y축에 있을 때 => a*k+b*k + 1(원점 포함)
2. 단, 두개의 합이 
"""
# import math
# def solution(k, d):
#     answer = 0
#     #x,y의 좌표들 구하기
#     x_li = []
#     y_li = []
#     for i in range(1,1000000):
#         x = k*i#2*1, 2*2, 2*3
#         y = k*i#2*1, 2*2
#         if x>d and y>d:
#             break
#         x_li.append(x)
#         y_li.append(y)
#     # print(x_li, y_li)
#     cnt = len(x_li)+len(y_li)+1
#     # print('cnt', cnt)
    
#     for x_val in x_li:#(2,4)
#         for y_val in y_li:#(2,2), (2,4), (4,2), (4,4)
#             a = (x_val**2+y_val**2)**(1/2)
#             if (x_val**2+y_val**2)**(1/2)<=d:
#                 cnt += 1
#                 # print(cnt, x_val, y_val, a)
#             else:
#                 continue

#     return cnt
'''
이중 for문 시간 오래걸림'''
# def solution(k, d):
#     answer = 0
    
#     for a in range(0, d + 1, k):
#         for b in range(0, d + 1, k):
#             if a**2 + b**2 <= d**2:
#                 answer += 1
    
#     return answer

def solution(k, d):
    answer = 0
    for x in range(0,d+1,k):
        res = int((d**2 - x**2)**0.5)#y의 최댓값
        # print(res)
        answer += (res // k) + 1        
        
    return answer