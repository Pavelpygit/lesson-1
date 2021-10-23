str_1 = input('введите любой текст с цифрами:  ')
for i in str_1:
    if i.isdigit():
        print(i, end=',')
