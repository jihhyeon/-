#문자와 숫자 분리 어떻게 하지?
lang = "AJKDLSI412K4JSJ9D"
a = list(lang)
num = 0
str_list = []
for i in a:
    if i.isnumeric() == True:
        num += int(i)
    else:
        str_list.append(i)

str_list = sorted(str_list)
str_list.append(str(num))#맨뒤에 삽입됨

for i in str_list:
    print(i, end = '')

