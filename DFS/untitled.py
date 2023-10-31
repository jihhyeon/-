import sys
n = int(sys.stdin.readline())

alpha = []
alpha_dict = {}
numlist = []

for i in range(n):
    alpha.append(sys.stdin.readline().rstrip())

#각 자리수를 지정하기(십의자리, 천의자리..)
for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict:
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
            # print(alpha_dict)
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)
            # print(alpha_dict)

for val in alpha_dict.values():
    numlist.append(val)

numlist.sort(reverse = True)
# print(numlist)

sum = 0
pows = 9
for i in numlist:
    sum += pows * i
    pows -= 1
print(sum)

