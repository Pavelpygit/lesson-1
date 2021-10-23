name_1 = input()
if name_1 == ('погода'):
    name_2=input('минск/москва')
    if name_2=='минск':
        name_3 = input('сегодня/завтра')
        if name_3=='сегодня':
            print(20)
        elif name_3=='завтра':
            print('28')
    elif name_2=='москва':
        name_3 = input('сегодня/завтра')
        if name_3 == 'сегодня':
            print(10)
        elif name_3 == 'завтра':
            print('18')
elif name_1 == ('дата'):
    print('29.08.2021')
elif name_1 == ('шутка'):
    print('колобок повесился')