answer = int(input('сколько Вам лет?  '))
if answer < 0:
    print('Wrong input')
elif answer < 18:
    print('CocaCola')
else:
    print('Beer')
