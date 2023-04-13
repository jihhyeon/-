"""폴리오미노 = aaaa, bb
x를 모두 폴리오미노로 덮으려 함 / .은 폴리오미노로 덮으면 안됨
폴리오미노로 모두 덮은 보드판 출력하기
1. .을 만나기 전까지의 x의 개수가 각각 폴리오미노 갯수와 같응ㄹ 때..?
"""
# a = "AAAA"
# b = "BB"
# array = str(input())
# answer = []
# real = []
# def greedy(answer):
#     new = []
#     n = len(answer)
#     if n >= len(a) and (n % 2 == 0):#4개보다 크고 2의 배수이면 => a,b섞어서 채우기
#         while answer:#"xxxxxx"
#             if len(answer)== 0:
#                 return new
#             elif len(answer)>=4:
#                 new.append(a * (len(answer)//4))
#                 del answer[0:4]

#                 if len(answer) == 2:
#                     new.append(b)
                    
#     elif n == len(b):
#         return "BB"
     
#     elif n % 2 != 0:
#         return -1


# for i in array:
#     if i == ".":
#         print(".", end = '')
#         answer = []
#     elif i == len(array)-1:
#         real.append(greedy(answer))

#     else:
#         answer.append(i)
#         print(answer)
#         print(greedy(answer), end = '')

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)