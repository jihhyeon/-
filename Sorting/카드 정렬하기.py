n = int(input())
card = []
for i in range(n):
    card.append(int(input()))
# card.sort()
# cnt = 0
# answer = 0
# while True:
#     if len(card) == 1:
#         break
#     else:
#         for _ in range(n-1):
#             # print(i, i+1)
#             cnt = card[0]+card[1]
#             answer += cnt
#             card.pop(0)
#             card.pop(0)
#             card.insert(0,cnt)
#             # print(card, cnt, answer)
# print(answer)
#----------------------------
import heapq
heapq.heapify(card)
cnt = 0

while len(card)>1:
    cnt_sum = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, cnt_sum)
    cnt += cnt_sum
print(cnt)


    