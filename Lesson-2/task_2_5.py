mon_1 = int(input('введите рубли:  '))
mon_2 = int(input('введите копейки:  '))
if mon_1 == 1:
    print(mon_1, 'рубль')
elif 1 < mon_1 <=4:
    print(mon_1, 'рубля')
else:
    print(mon_1, 'рублей')
if 1 < mon_2 <= 4:
    print(mon_2,'копейки')
else:
    print(mon_2, 'копеек')
    # работает только до 20 р и 20коп. 21,22...24 нужно склонять снова и так со всеми десятками. Как реализовать?
    # предполагаю что через in как в первом задании, но у меня не вышло.